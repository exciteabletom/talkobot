from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer as Trainer

def get_chatbot():
	bot = ChatBot(
		"Chats",
		database_uri = "sqlite:///database.sqlite3",
		logic_adapters=[
			'chatterbot.logic.BestMatch',
			'chatterbot.logic.MathematicalEvaluation',
			'chatterbot.logic.TimeLogicAdapter',
		],
	)

	trainer = Trainer(bot)

	trainer.train(
		"chatterbot.corpus.english",
	)

	return bot

