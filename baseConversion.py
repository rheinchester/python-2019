def baseConversion(num, base):
	# convert binary number of any base to decimal
	convert = 0
	numLength = 0
	digit = len(num)-1
	while numLength < len(num):
		conversion = int(num[numLength]) * (base ** digit)
		convert += conversion
		numLength += 1
		digit -= 1
	return convert

def numOfBinaryOnes(num):
	# get the number of ones in a binary
	try:
		for digit in num:
			intDigit = int(digit)
			if int(digit) > 1:
				return 'Not a binary'
	except ValueError:
		return 'Wrong input'
	return baseConversion(str(num), 1)
	
print(numOfBinaryOnes('1010x10101010'))
