import time

def fib(n):
	if n == 1:
		return 0
	
	if n == 2:
		return 1
	
	return fib(n - 1) + fib(n - 2)

start_time = int(round(time.time() * 1000))

print(fib(10))

end_time = int(round(time.time() * 1000))
print("Time spent: ", end_time - start_time)


dpList = {}
def dpfib(n):
	if n == 1:
		return 0

	if n == 2:
		return 1

	if n in dpList:
		return dpList[n]
	
	dpList[n] = dpfib(n - 1) + dpfib(n - 2)

	return dpList[n]

start_time = int(round(time.time() * 1000))

print(dpfib(10))

end_time = int(round(time.time() * 1000))
print("Time spent: ", end_time - start_time)


def dpfib1(n):
	dp = []
	dp.append(0) 
	dp.append(1) 
	for i in range(2, n + 1):
		dp.append(dp[i - 1] + dp[i - 2])
	return dp[n]

start_time = int(round(time.time() * 1000))

print(dpfib(10))

end_time = int(round(time.time() * 1000))
print("Time spent: ", end_time - start_time)


