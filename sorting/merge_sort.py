def merge_sort(arr):
	merge_sort2(arr, 0, len(arr) - 1)
def merge_sort2(arr, start, end):
	if start < end:
		n = start + (end - start)//2
		merge_sort2(arr, start, n)
		merge_sort2(arr, n + 1, end)
		merge(arr, start, n, end)
def merge(arr, start, n, end):
	temp = []
	i = start
	j = n + 1
	while(i <= n and j <= end):
		if arr[i] <= arr[j]:
			temp.append(arr[i])
			i = i + 1
		else:
			temp.append(arr[j])
			j = j + 1
	while j <= end:
		temp.append(arr[j])
		j = j + 1
	while i <= n:
		temp.append(arr[i])
		i = i + 1
	k = 0
	for i in range(start, end + 1):
		arr[i] = temp[k]
		k = k + 1
unsorted_array = [5,9,1,3,5,2,0,1,7,4]
merge_sort(unsorted_array)
print(unsorted_array)