from chatterbot import ChatBot, filters, comparisons, response_selection
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import logging

import parse

logging.basicConfig(level=logging.INFO)


def get_chatbot():
	bot = ChatBot(
		"Talko the bot",
		database_uri="sqlite:///database.sqlite3",
		logic_adapters=[
			{
				"import_path": "chatterbot.logic.BestMatch",
				"statement_comparison_function": comparisons.levenshtein_distance,
				"response_selection_method": response_selection.get_random_response,
			},
			'chatterbot.logic.MathematicalEvaluation',
		],
		read_only=True,
		filters=[filters.get_recent_repeated_responses],
	)

	return bot


def train_chatbot():
	bot = get_chatbot()

	list_trainer = ListTrainer(bot)

	list_trainer.train(parse.movie_lines())

	corpus_trainer = ChatterBotCorpusTrainer(bot)

	corpus_trainer.train(
		"chatterbot.corpus.english",
	)


if __name__ == "__main__":
	train_chatbot()
