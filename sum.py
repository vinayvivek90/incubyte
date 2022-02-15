def Add(str):
	if str == "":
		return 0
	str = str.replace('\n',',')
	values = str.split(',')
	total = 0
	for i in values:
		total += int(i)
	return total