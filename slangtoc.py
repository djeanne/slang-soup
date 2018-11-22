#!/usr/bin/env python3

def slang_dict_toc(): 
	from string import ascii_lowercase

	slangpages = []

	for c in ascii_lowercase:
		slang = "http://www.peevish.co.uk/slang/" + c + ".htm"
		slangpages.append(slang)

	return slangpages
	
if __name__ == "__main__":
	slangpages = slang_dict_toc()
	print(slangpages)