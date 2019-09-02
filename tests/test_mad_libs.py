import mad_libs

def test_get_tags():
	tag = 'this stuff (dont break)'
	text = f'This is an example to get [{tag}]'
	assert mad_libs.get_tags(text) == [tag]


if __name__ == '__main__':
	test_get_tags()
