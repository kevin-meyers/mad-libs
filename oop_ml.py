import random
import re

from collections import defaultdict




class MadLibs:

    def __init__(self, text, shuffle=True):
        self.text = text
        self.tags = self.get_tags()
        self.shuffle = shuffle
        self.responses = defaultdict(lambda: [])


    def run(self):
		make_questions()
		if shuffle:
			randomize()
		build_story()
		return self.text

	def make_questions(self):
        for tag in self.tags:
            self.responses[tag].append(self.ask_pos(tag))


    def randomize(self):
            for key in self.responses.keys():
                random.shuffle(self.responses[key])
	
	def build_story(self):
        for tag in self.tags:
            tag_escaped = re.escape('[' + tag + ']')
            word = self.responses[tag].pop()

            self.text = re.sub(tag_escaped, word, self.text, count=1)

    def get_tags(self):
        return re.findall(r'(?<=\[).+?(?=\])', self.text)

    @staticmethod
    def ask_pos(pos):  # Parts Of Speech
        return input(f'Enter a(n): {pos}\n')

if __name__ == '__main__':
	text = open('example.txt').read()
	m = MadLibs(text=text)
	
	m.run()
