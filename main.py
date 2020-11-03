import time

import amanobot  # telegram bot lib
import random
from amanobot.loop import MessageLoop  # loop to check for messages

from train import get_chatbot
from var import BOT_NAME
from private import prod_token


chat_backend = get_chatbot()

def main_loop(msg):
	content_type, chat_type, chat_id = amanobot.glance(msg)

	if content_type == "text":
		msg_text = msg["text"].lower() 
		check = True
		# In a group always respond when mentioned
		# or respond 10% of the time
		if chat_type == "group" and not random.random() < 0.05:
			check = BOT_NAME in msg_text

		if check:
			msg_text = msg_text.replace(BOT_NAME, "").strip()
			resp = chat_backend.get_response(msg_text)
			resp = str(resp)

			bot.sendMessage(chat_id, resp)
			

bot = amanobot.Bot(prod_token)
MessageLoop(bot, main_loop).run_as_thread()

while True:
	time.sleep(10)

