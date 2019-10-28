def recur(start, end):
	m = (start + end)/2
	if m > start:
		recur(start, m - 1)
recur(3, 199)