def linearSearch (arr, m):
	for i in range(0, len(arr)):
		if arr[i] == m:
			return i
		elif arr[i] > m:
			break
	return -1
print(linearSearch ([1,9,23,34,39,45,56,67,69,73,75,81,89,91], 29))
print(linearSearch ([8, 9, 23, 56, 71, 81, 93, 102], 56))



