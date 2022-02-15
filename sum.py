def sum(str):
	if str == "":
		return 0
	elif len(str) == 1 and str.isnumeric():
		return int(str)