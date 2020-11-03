import json


def telegram():
	f = open("./result.json", "r")
	data = json.load(f)
	f.close()

	chat_lists = []

	# Buffer for multiline messages
	buffer = ""

	for chat in data["chats"]["list"]:
		chat_lists.append([])
		for message in chat["messages"]:
			# HACK: Convert message to ascii
			try:
				message["text"] = message["text"].encode("ascii", errors="ignore").decode()
			except:
				pass

			if message["type"] == "message" and message["text"] and type(message["text"]) == str:
				if "\n" not in message["text"] and buffer:
					buffer += message["text"]
					chat_lists[-1].append(buffer)
					buffer = ""
				elif "\n" in message["text"]:
					buffer += message["text"]
				else:
					chat_lists[-1].append(message["text"])

	return chat_lists


def movie_lines():
	f = open("./movie_lines.txt", "r")
	data = f.read()
	f.close()
	sep = "+++$+++"
	lines = data.split("\n")
	processed = []

	# Strip metadata
	for line in lines:
		processed.append(line.split(sep)[-1])

	return processed

