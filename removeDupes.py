def removeRepeats(inputString):
	seen = []
	for x in xrange(len(inputString)):
		if inputString[x] not in seen:
			seen.append(inputString[x])
		else:
			continue
	return seen

a = "abba"
print removeRepeats(a)