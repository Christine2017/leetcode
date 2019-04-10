# input is binary int
def numberOfOneBits(n):
	num_bits = 0
	while n != 0:
		num_bits += (n & 1)
		n >>= 1
	return num_bits

n = 0b100100
# print numberOfOneBits(n)
# Tn = O(n)
# n is the number of bits in the input integer

# follow up 1: check parity


