import sys
import json

def getAllTerms():
	with open(sys.argv[1], 'r') as content_file:
		paragraph = content_file.read()

	list_terms = paragraph.split()
	terms_hash = {}

	for idx,term in enumerate(list_terms):
		if term not in terms_hash:
			terms_hash[term] = [idx]
		else:
			terms_hash[term].append(idx)

	with open('output.json', 'w') as f:
		f.write(json.dumps(terms_hash))

getAllTerms()