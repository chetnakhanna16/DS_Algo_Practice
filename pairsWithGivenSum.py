def pairsWithGivenSum(arr, x):
	hs = set()
	for i in range(0, len(arr)):
		temp = x - arr[i]
		if temp in hs:
			print (arr[i], temp)
		else:
			hs.add(arr[i])
print(pairsWithGivenSum([1, 5, 3, 19, 21, 8, 7, 11, 21, 15, 17], 14))
print(pairsWithGivenSum([5, 6, 9, 11, 13, 27, 15], 25))
print(pairsWithGivenSum([4, 5, 6, 1, 11, 9, 3, 7], 10))
print(pairsWithGivenSum([6, 14, 13, 8, 9, 10, 12, 43, 67, 32], 42))