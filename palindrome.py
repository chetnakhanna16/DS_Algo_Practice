def palindrome(num):
	i = 0
	j = len(num) - 1
	while i < j:
		if num[i] == num[j]:
			i = i + 1
			j = j - 1
		else: 
			return False
	return True

print(palindrome("12321"))
print(palindrome("91833819"))
print(palindrome("67812876"))
print(palindrome("198263"))
