def sumOfTwo1(arr, x):
	hs = set()
	for i in range(0, len(arr)):
		temp = x - arr[i]
		if temp in hs:
			print (arr[i], temp)
			return True
		else:
			hs.add(arr[i])
	return False
print(sumOfTwo1([1, 5, 3, 19, 21, 8, 7, 11, 21, 15, 17], 14))
print(sumOfTwo1([5, 6, 9, 11, 13, 27, 15], 25))
print(sumOfTwo1([4, 5], 10))
print(sumOfTwo1([6, 14, 13, 8, 9, 10, 12, 43, 67, 32], 42))