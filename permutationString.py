def permute(given):
	permute_advance(given, "", [])

def permute_advance(given, curr, lst):
	if len(curr) == len(given):
		print(curr)
		return

	for i in range(len(given)):
		if i not in lst:
			lst.append(i)
			permute_advance(given, curr + given[i], lst)
			del lst[-1]

permute("united")
