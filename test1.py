text_data = []
namescount = {}
f = open('input.txt', 'r')
for names in f.read().split():
	if names not in namescount:
		namescount[names] = 1
	else:
		namescount[names] + = 1 
for k,v in namescount.items():
	print k, v
