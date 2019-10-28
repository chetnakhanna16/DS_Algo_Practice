def insertion_sort(arr):
	for i in range (1, len(arr)): #Take i from 1 as for 0 we will not have anything to compare
		j = i - 1
		while j >= 0:
			if arr[j+1] < arr[j]:
				value = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = value
				j = j - 1
			else:
				break
	return arr
print(insertion_sort([1,6,9,3,2,5]))
print(insertion_sort([3,1,9,10,2,3,5,4,9,8]))