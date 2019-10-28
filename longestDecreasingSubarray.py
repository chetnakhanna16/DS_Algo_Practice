def longestDecreasingSubarray(arr):
	if len(arr) == 0:
		return 0

	i = 1
	min_count = 1
	count = 1
	while i < len(arr):
		if arr[i - 1] >= arr[i]:
			count = count + 1
			i = i + 1
		else:
			min_count = max(count, min_count)
			count = 1
			i = i + 1
	return min_count

print(longestDecreasingSubarray([1,3,4,2,0,8,6,5,2,1]))
print(longestDecreasingSubarray([1,3,4,0,6,7,5,6,9]))

