import csv

existingwords = ["assess",
				"aware",
				"battalion",
				"biological",
				"bring",
				"burnt",
				"catholic",
				"chain",
				"classical",
				"common",
				"conversion",
				"crack",
				"credible",
				"current",
				"dance",
				"diploma",
				"dramatist",
				"dying",
				"effect",
				"exercise",
				"experiment",
				"explode",
				"fashionable",
				"feature",
				"few",
				"folklore",
				"force",
				"fuss",
				"girl",
				"gold",
				"guidance",
				"hang",
				"idiom",
				"imagination",
				"improvement",
				"innocent",
				"kitchen",
				"knowledge",
				"lemon",
				"let",
				"loss",
				"ma",
				"money",
				"mouth",
				"mush",
				"need",
				"nervous",
				"noun",
				"owe",
				"percentage",
				"plenty",
				"rang",
				"rare",
				"remote",
				"restoration",
				"rest",
				"revolution",
				"rude",
				"scope",
				"seat",
				"small",
				"society",
				"space",
				"spare",
				"spy",
				"strike",
				"stuck",
				"sum",
				"talent",
				"tax",
				"told",
				"ton",
				"truth",
				"two",
				"use",
				"warm",
				"wedlock",
				"window",
				"winter",
				"wooden"
				]

formattedExistingWords = []

for e in existingwords:
	formattedExistingWords.append(e.upper())

formattedExistingWords = set(formattedExistingWords)
newWords = []

with open('corpus-original.csv', 'r') as f:
		reader = csv.reader(f)
		for r in reader:
			newWords.append(r)
		for w in newWords:
			for e in formattedExistingWords:
				if e == w[0]:
					newWords.remove(w)

newWords = set(newWords)
with open('corpus-revamp.csv','w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(newWords) 					

print newWords