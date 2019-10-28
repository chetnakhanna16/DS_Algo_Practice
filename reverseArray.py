def reverseArray(arr):
	i = 0
	j = len(arr) - 1
	while i < j:
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		i = i + 1
		j = j - 1
	return arr
print(reverseArray([2,5,9,18,2,13,1,19,91,45,67]))