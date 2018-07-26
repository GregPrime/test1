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
if len(sys.argv) == 2:
	if sys.argv[1] == 'sort':
		counts = sorted(counts)
		for (names, count) in counts.items():
			print('{:20}{:3}'.format(names, count))
else:
	for names in text_data:
		print names, counts[names]

