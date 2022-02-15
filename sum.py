def Add(str):
	if ',\n' in str or '\n,' in str:
		return 'bad input'
	str = str.replace('\n',',')
	values = str.split(',')
	total = 0
	for i in values:
		if i == '':
			i = '0'
		total += int(i)
	return total