def longestSameSubarray(arr):
	count = 0
	i = 0
	j = 1
	if len(arr) == 0:
		temp = 0
	else:
		temp = 1
	while i < len(arr) and j < len(arr): 
		if arr[i] == arr[j]:
			temp = temp + 1
			j = j + 1
		else:
			temp = 1
			i = j
			j = i + 1
		count = max(count, temp)
	count = max(count, temp)
	return (count)
print(longestSameSubarray([1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7]))
print(longestSameSubarray([1]))
print(longestSameSubarray([]))
print(longestSameSubarray([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7]))
