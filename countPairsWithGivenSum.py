def countPairsWithGivenSum(arr, x):
	hs = set()
	count = 0
	for i in range(0, len(arr)):
		temp = x - arr[i]
		if temp in hs:
			count = count + 1
		else:
			hs.add(arr[i])
	return(count)
print(countPairsWithGivenSum([1, 5, 3, 19, 21, 8, 7, 11, 21, 15, 17], 14))
print(countPairsWithGivenSum([5, 6, 9, 11, 13, 27, 15], 25))
print(countPairsWithGivenSum([4, 5, 6, 1, 11, 9, 3, 7], 10))
print(countPairsWithGivenSum([6, 14, 13, 8, 9, 10, 12, 43, 67, 32], 42))
