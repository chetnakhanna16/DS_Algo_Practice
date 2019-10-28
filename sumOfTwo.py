def sumOfTwo(arr, x):
	for i in range (0, len(arr)):
		for j in range (i + 1, len(arr)):
			if arr[i] + arr[j] == x:
				print (arr[i], arr[j])
				return True
				break	
	return False
print(sumOfTwo([1, 5, 3, 19, 21, 8, 7, 11, 21, 15, 17], 14))
print(sumOfTwo([5, 6, 9, 11, 13, 27, 15], 25))
print(sumOfTwo([4, 5], 10))
print(sumOfTwo([6, 14, 13, 8, 9, 10, 12, 43, 67, 32], 42))