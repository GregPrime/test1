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
counts_list = counts.keys()
# If user execute test1.py with arg 'sort'
if len(sys.argv) == 2:
	if sys.argv[1] == 'sort':
		counts_list = sorted(counts_list)
		for names in counts_list:
			print('{:20}{:3}'.format(names,counts[names])) 
else:
	for names in text_data:
		print names, counts[names]

