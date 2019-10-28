def bubble_sort(arr):
	for i in range (0, len(arr)-1):
		for j in range (0, len(arr)-i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp
	print (arr)
bubble_sort([2,7,1,4,5,3])
bubble_sort([8,2,5,7,1,3,4,5,3,9])
bubble_sort([7,1,1,4,3,5,6,3,9])