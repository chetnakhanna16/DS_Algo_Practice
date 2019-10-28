def validBracketString(str):
	countopen = 0

	if len(str) == 0:
		return True

	if str[0] == ")":
		return False

	for i in range (0, len(str)): 
	 	if str[i] == "(":
	 		countopen = countopen + 1
	 	elif str[i] == ")":
	 		if countopen > 0:
	 			countopen = countopen - 1
	 		else:
	 			return False
	if countopen == 0:
		return True
	return False

print(validBracketString("(()(()()()(()))()"))
print(validBracketString(")((())(("))
print(validBracketString("())("))
print(validBracketString("(())()()"))


