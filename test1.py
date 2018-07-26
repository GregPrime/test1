from collections import Counter
text_data = []
f = open('input.txt', 'r')
for line in f.readlines():
	text_data = text_data + line.split()
counts = Counter(text_data)
for names in text_data:
	print names, counts[names]