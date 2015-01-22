def altStr(inString, length):
	length = length - 1
	for i in xrange(length):
		currPos = length - i
		if inString[currPos] == " ":
			inString = inString[:currPos] + "%20" + inString[currPos + 1 :]
	print inString

altStr("Mr John Smith        ", 13)