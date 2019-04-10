# parity is 1 if number of 1s in the binary word is odd
# else is 0
# AIM: check accurate data transmission between nodes during communication

# input is binary int
### basic Tn = O(n)
def check_parity(n):
	result = 0
	while n != 0:
		result ^= (n & 1)
		n >>= 1
	return result
n = 0b100100
# print check_parity(n)


### improve 1 Tn = O(k), k is the number of 1s in n
def check_parity_1(n):
	result = 0
	while n != 0:
		result ^= 1
		n = n & (n - 1) # delete last 1 in n
	return result


### improve 2 Tn = O(logn)

