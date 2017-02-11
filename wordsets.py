import csv
import random

def main():
	# raw_input updated to input in python 3
	n = int(input("How many words in each set? \n"))
	s = int(input("How many sets? \n"))
	m = int(input("What should the median of each set be? \n"))
	r = int(input("What should the range of the median be? \n"))
	f = input("what is the path to the file? \n")

	make_sets(n, s, m, r, f)

#----------------------------------------------------------------------
# Makes n number of sets with the indicated median +- range 
# using the words in the csv File. The function returns a nested
# dictinary where the value of each 'Set#' key contains the set
#
# takes: Int, Int, Int, Int, Str
# returns: Dict
def make_sets(n, sets, median, r, csvPath):
	words = store_words(csvPath)
	wordsets = {}

	for i in range(sets):
		wordsets['Set' + str(i+1)] = make_set(n, median, r, words)

	print(wordsets['Set1'])

#----------------------------------------------------------------------
# Takes csvFile, store each row into the dictionary as a
# key-value pair (word-frequency)
#
# takes: String
# returns: Dictionary
def store_words(csvPath):
	words = {}
	with open(csvPath) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			words[row['WORD'].strip()] = int(row['BROWN_FREQ'])

	return words

#----------------------------------------------------------------------
# Makes a single set of given n, median, and range
#
# takes: Int, Int, Int, Dict
# returns: Dict
def make_set(n, median, r, words):
	frequencies = list(words.values())
	wordlist = list(words.keys())
	wordset = {}
	
	if n % 2 == 0:
		initials = find_initial_indices(2, frequencies, median, r)
		smaller = random.sample(range(initials[0]), int((n-2)/2))
		greater = random.sample(range(initials[1]+1, len(frequencies)), int((n-2)/2))
		indices = initials + greater + smaller
	else:
		initial = find_initial_indices(1, frequencies, median, r)
		smaller = random.sample(range(initials[0]), int((n-1)/2))
		greater = random.sample(range(initials[1]+1, len(frequencies)), int((n-1)/2))
		indices = initials + greater + smaller

	for i in indices:
		wordset[wordlist[i]] = frequencies[i]

	delete_items(words, indices)

	return wordset

#----------------------------------------------------------------------
# Produces the indices of intitial words in a list
#
# takes: Int, List
# returns: List
def find_initial_indices(E_O, frequencies, median, r):
	if E_O == 2:
		initial_range = [i for i, x in enumerate(frequencies) if (x >= median-r and x <= median+r)]
		initial_indices = sorted(random.sample(initial_range, 2))
	elif E_O == 1: 
		initial_range = [i for i, x in enumerate(frequencies) if (x >= median-r and x <= median+r)]
		initial_indices = sorted(random.sample(initial_range, 1))

	return initial_indices
#----------------------------------------------------------------------
# Delete the key-value pairs in the dictinoary
#
# takes: Dict, List
# returns: none
def delete_items(words, indices):
	wordlist = list(words.keys())
	for i in indices:
		del words[wordlist[i]]

main()

# tested this
# make_sets(10,4,100,50,'corpus.csv')