import sys
from collections import Counter
#Read initial names from file
text_data = []
f = open('input.txt', 'r')
for line in f.readlines():
	text_data = text_data + line.split()
f.close()
# counts of duplicate names
counts = Counter(text_data)
# If user execute test1.py with arg 'sort'
if sys.argv[1] == 'sort':
	text_data = sorted(text_data)
	maxlength = max(len(s) for s in text_data)
	for names in text_data:
		text_data[names] = '{:<{maxlength}}'.format(names)

#Print results

for names in text_data:
	print names, counts[names]

