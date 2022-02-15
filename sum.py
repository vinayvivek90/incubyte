def Add(str):
	if str == "":
		return 0
	elif len(str) == 1 and str.isnumeric():
		return int(str)
	else:
		values = str.split(',')
		total = 0
		for i in values:
			total += int(i)
		return total