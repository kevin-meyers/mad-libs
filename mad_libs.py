import re

from collections import defaultdict
from random import shuffle


def get_tags(text):
	return re.findall(r'(?<=\[).+?(?=\])', text)

def to_question(tag):
	return f'Enter a(n): {tag}'

def make_questions(tags):
	return [(tag, to_question(tag)) for tag in tags]

def randomize(responses):
	[shuffle(responses[key]) for key in responses.keys()]
	return responses

def build_story(text, tags, responses):
	for tag in tags:
		tag_escaped = re.escape('[' + tag + ']')
		word = responses[tag].pop()

		text = re.sub(tag_escaped, word, text, count=1)
	return text.split('\n')

