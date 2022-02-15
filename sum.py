def Add(array):
	if ',\n' in array or '\n,' in array:
		return 'bad input'
	if array[:2] == '//':
		delimiter = array[2]
		array = array[4:]
	else:
		delimiter = ','
	array = array.replace('\n',delimiter)
	values = array.split(delimiter)
	total = 0
	for i in values:
		if i == '':
			i = '0'
		total += int(i)
	return total
	