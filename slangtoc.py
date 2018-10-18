from string import ascii_lowercase

slangpages = []
for c in ascii_lowercase:
	slang = "http://www.peevish.co.uk/slang/" + c + ".htm"
	slangpages.append(slang)
	