def selection_sort(arr):
	for i in range (0, len(arr)-1):
		min_index = i
		for j in range (i+1, len(arr)):
			if arr[j] < arr[min_index]:
				temp = arr[j]
				arr[j] = arr[min_index]
				arr[min_index] = temp
	print(arr)
selection_sort([2,7,4,1,5,3])
selection_sort([9,5,2,7,4,1,5,6,3])
selection_sort([4,2,7,4,1,5,10,12,3])
