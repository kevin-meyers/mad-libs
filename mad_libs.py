class MadLibs(text, shuffle = False):
    
    def get_tags(string):
        return re.findall(r'(?<=\[).+?(?=\])', string)
    
    def ask_pos(pos):  # Parts Of Speech
        return input(f'Enter a(n): {pos}\n')
    
    tags = get_tags(text)

    responses = defaultdict(lambda: [])
    
    for tag in tags:
        responses[tag].append(ask_pos(tag))

    if shuffle:
        for key in responses.keys():  # Maybe call key, pos
            random.shuffle(responses[key])

    for tag in tags:
        tag_escaped = re.escape('[' + tag + ']')
        word = responses[tag].pop()
        
        text = re.sub(tag_escaped, word, text, count=1)
    
	print(text)

if __name__ == '__main__':
	text = open('example.txt')
	m = MadLibs(text)
