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
	for value in values:
		if value == '':
			value = '0'
		elif int(value) <0:
			break
		total += int(value)
	negative = ''
	for value in values:
		if value == '':
			value = '0'
		elif int(value)<0:
			negative += ' '+value
	if len(negative)>0:
		return 'negatives not allowed '+negative
	return total
