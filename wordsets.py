import csv
import random
import datetime


def main():
	# raw_input updated to input in python 3
	n = int(input("How many words in each set? \n"))
	s = int(input("How many sets? \n"))
	a = int(input("What should the average of each set be? \n"))
	d = int(input("What should the permissible deviation from the average be? \n"))
	f = input("what is the path to the file? \n")

	wordsets = make_sets(n, s, a, d, f)
	write_to_csv(wordsets)
	writeparameters(n,s,a,d,f)

#----------------------------------------------------------------------
# Makes n number of sets with the indicated median +- range 
# using the words in the csv File. The function returns a nested
# dictinary where the value of each 'Set#' key contains the set
#
# takes: Int, Int, Int, Int, Str
# returns: Dict
def make_sets(n, sets, average, pdfa, csvPath):
	words = store_words(csvPath)
	wordsets = {}

	for i in range(sets):
		wordsets['Set' + str(i+1)], indices = make_set(n, average, pdfa, words)
		delete_items(words, indices)

	# print(wordsets)
	return wordsets

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
# Makes a single set of given n, average, and pdfa, and the
# indices that comprise the set
#
# takes: Int, Int, Int, Dict
# returns: Dict, List
def make_set(n, average, pdaf, words):
	frequencies = list(words.values())
	wordlist = list(words.keys())
	wordset = {}
	sum_randoms = (average+pdaf)*n + 1
	lower_bound = (average-pdaf)*n
	upper_bound = (average+pdaf)*n

	# pick n-1 random words
	while sum_randoms >= upper_bound :
		randoms = random.sample(range(len(frequencies)), n-1)
		# results = list(map(int, randoms))
		s = 0
		for i in randoms:
			s +=frequencies[i]
		if s < upper_bound:
			sum_randoms = s
	# print("sum: " + str(sum_randoms))
	# print("sum range:" + str(lower_bound) + " - " + str(upper_bound))
	
	last_range = [i for i, x in enumerate(frequencies) 
					if (x >= (lower_bound-sum_randoms) and x <= (upper_bound-sum_randoms))]
	# pick last word randomly within possible range
	last = random.sample(last_range, 1)
	# print("last: " + str(frequencies[last[0]]))
	indices = randoms + last

	for i in indices:
		wordset[wordlist[i]] = frequencies[i]
	
	return wordset, indices


	# if n % 2 == 0:
	# 	initials = find_initial_indices(2, frequencies, median, r)
	# 	smaller = random.sample(range(initials[0]), int((n-2)/2))
	# 	greater = random.sample(range(initials[1]+1, len(frequencies)), int((n-2)/2))
	# 	indices = initials + greater + smaller
	# else:
	# 	initial = find_initial_indices(1, frequencies, median, r)
	# 	smaller = random.sample(range(initials[0]), int((n-1)/2))
	# 	greater = random.sample(range(initials[1]+1, len(frequencies)), int((n-1)/2))
	# 	indices = initials + greater + smaller

	# for i in indices:
	# 	wordset[wordlist[i]] = frequencies[i]

	# return wordset, indices

#----------------------------------------------------------------------
# Produces the indices of intitial words in a list
#
# takes: Int, List
# returns: List
# def find_initial_indices(E_O, frequencies, median, r):
# 	if E_O == 2:
# 		initial_range = [i for i, x in enumerate(frequencies) if (x >= median-r and x <= median+r)]
# 		initial_indices = sorted(random.sample(initial_range, 2))
# 	elif E_O == 1: 
# 		initial_range = [i for i, x in enumerate(frequencies) if (x >= median-r and x <= median+r)]
# 		initial_indices = sorted(random.sample(initial_range, 1))

# 	return initial_indices
#----------------------------------------------------------------------
# Delete the key-value pairs in the dictinoary
#
# takes: Dict, List
# returns: none
def delete_items(words, indices):
	wordlist = list(words.keys())
	for i in indices:
		del words[wordlist[i]]

#----------------------------------------------------------------------
# Writes to .csv file
#
# takes: Dict
# returns: none
def write_to_csv(wordsets):
	sets = list(wordsets.keys())
	l = []
	
	# create columns as lists and append to l
	for i in sets:
		words = [i] + list(wordsets[i].keys())
		frequencies = [''] + list(wordsets[i].values())
		divider = [''] * len(words)
		l.append(words)
		l.append(frequencies)
		l.append(divider)
	
	# transpose l
	l = list(map(list, zip(*l)))

	with open('wordsets.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(l)

def writeparameters(size, sets, ave, pdfa, path):
	date = datetime.date.today().strftime("%B %d, %Y")
	datestr = "file written on: "+str(date)+"\n"
	filestr = "file: "+str(path)+"\n"
	setstr = "set size: "+str(size)+"\n"
	numsetstr = "number of sets: "+str(sets)+"\n"
	avestr = "targeted ave: "+str(ave)+"\n"
	pdfastr = "permissible deviation from ave: "+str(pdfa)+"\n"

	text = datestr+filestr+setstr+numsetstr+avestr+pdfastr

	tf = open("parameters"+date+".txt", "w")
	tf.write(text)
	tf.close()

# main()

# tested this (can also just use this)
wordsets = make_sets(10,4,775,50,'corpus.csv')	
write_to_csv(wordsets)