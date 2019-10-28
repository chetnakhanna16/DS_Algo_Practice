def validMultiBracketString(s):
	if len(s) == 0:
		return True

	stack = []
	pairs = {"(":")", "{":"}", "[":"]"}

	for paranthese in s:
		if paranthese in pairs:
			stack.append(paranthese)
		elif len(stack) == 0 or pairs[stack.pop()] != paranthese:
			return False

	if len(stack) != 0:
		return False

	return True

print(validMultiBracketString("({}[])()({()})}"))
print(validMultiBracketString("{([])}({[]})"))
print(validMultiBracketString("{([)}]({[])}"))
print(validMultiBracketString("(]"))
print(validMultiBracketString("{([])}{[]})"))
print(validMultiBracketString("{([])}({[]}"))