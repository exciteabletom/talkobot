import time

import telepot  # telegram bot lib
from telepot.loop import MessageLoop  # loop to check for messages

from train import get_chatbot
from var import BOT_NAME
from private import prod_token


chat_backend = get_chatbot()

def main_loop(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	msg_text = msg["text"].lower() 
	print(msg_text)

	if content_type == "text" and BOT_NAME in msg_text:
		msg_text = msg_text.replace(BOT_NAME, "")
		resp = str(chat_backend.get_response(msg_text))

		bot.sendMessage(chat_id, resp)
			

bot = telepot.Bot(prod_token)
MessageLoop(bot, main_loop).run_as_thread()

while True:
	time.sleep(10)

