def recurse(inNum):
	currSum = inNum + 5
	if currSum >1000: #Base Case
		return currSum #Up the stack we go

	return recurse(currSum)

print recurse(0)