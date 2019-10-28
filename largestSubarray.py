def largestSubarray(arr):
	if len(arr) == 0:
		return 0

	i = 1
	max_count = 1
	count = 1
	while i < len(arr):
		if arr[i - 1] <= arr[i]:
			count = count + 1
			i = i + 1
		else:
			max_count = max(count, max_count)
			count = 1
			i = i + 1
	return max_count

print(largestSubarray([1,9,2,3,9,5,6,1,7,9,19,20,5,3,1]))

