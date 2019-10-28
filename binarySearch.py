def binarySearch (arr, t):
	return binarySearch2 (arr, 0, len(arr) - 1, t)

def binarySearch2 (arr, start, end, t):
	if start <= end:
		mid = start + ((end - start)//2)
		if arr[mid] == t:
			return mid
		elif arr[mid] > t:
			return binarySearch2 (arr, start, mid - 1, t)
		else:
			return binarySearch2 (arr, mid + 1, end, t)
	return -1

print (binarySearch ([1,6,12,13,19,32,76,91], 45))
print (binarySearch ([1,16,32,43,119,312,746,911,982,999], 999))
print (binarySearch ([11,61,112,113,129,132,136], 145))

