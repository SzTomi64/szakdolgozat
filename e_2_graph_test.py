import math

def possible_values(n):
	squares = [s**2 for s in range(2, int(math.sqrt(n))+1)]
	possible_values = []
	for s in squares:
		possible_values.append(s-1)
		possible_values.append(s+1)
	return possible_values

def primes_up_to_n(n):
	primes = [2]
	for i in range(3, n+1):
		for p in primes:
			if i%p==0:
				break
			if p>int(math.sqrt(i)):
				primes.append(i)
				break
	return primes

def factorise(n, primes):
	factors_0={p:0 for p in primes}
	while n>1:
		for p in primes:
			if n%p==0:
				n = int(n/p)
				factors_0[p]+=1
				break
	factors = {}
	for p in factors_0.keys():
		if factors_0[p]!=0:
			factors[p]=factors_0[p]
	return factors

def square_free_part(factors):
	square_free = []
	for p in factors.keys():
		if factors[p]%2==1:
			square_free.append(p)
	return square_free



def s_test(n):
	primes = primes_up_to_n(n)
	test_values = possible_values(n)
	probable_s = []
	for s in test_values:
		match s%8:
			case 0:
				factors = factorise(s-1, primes)
				sfp = square_free_part(factors)
				ind = True
				for p in sfp:
					if p%8==3 or p%8==5:
						ind = False
				if ind:
					probable_s.append(s)
			case 1:
				factors = factorise(s+1, primes)
				sfp = square_free_part(factors)
				ind = True
				for p in sfp:
					if p%8==3:
						ind = False
				if ind:
					probable_s.append(s)
			case 2:
				probable_s.append(s)
			case 3:
				factors = factorise(s-1, primes)
				sfp = square_free_part(factors)
				ind = True
				for p in sfp:
					if p%8==5 or p%8==7:
						ind = False
				if ind:
					probable_s.append(s)
			case 5:
				probable_s.append(s)
			case 7:
				factors = factorise(s-1, primes)
				sfp = square_free_part(factors)
				ind = True
				for p in sfp:
					if p%8==3 or p%8==5:
						ind = False
				if ind:
					probable_s.append(s)
	return probable_s

print(s_test(100))