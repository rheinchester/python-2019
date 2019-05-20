def baseConversion(num, base):
	convert = 0
	numLength = 0
	digit = len(num)-1
	while numLength < len(num):
		conversion = int(num[numLength]) * (base ** digit)
		convert += conversion
		numLength += 1
		digit -= 1
	return convert
print(baseConversion('123', 8))

