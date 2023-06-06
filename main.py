import math
import sympy


def A000004():
	while True:
		yield 0

def A000007():
	a = 0
	while True:
		yield int(a==0)
		a += 1

def A000012():
	while True:
		yield 1

def A000027():
	a = 0
	while True:
		a += 1
		yield a

def A000030():
	a = 0
	while True:
		yield int(str(a)[0])
		a += 1

def A000034():
	a = 0
	while True:
		yield a%2+1
		a += 1

def A000035():
	a = 0
	while True:
		yield a%2
		a += 1

def A000037():
	a = 0
	while True:
		if not math.sqrt(a).is_integer():
			yield a
		a += 1

def A000040():
	a = 0
	while True:
		if sympy.isprime(a):
			yield a
		a += 1

def A000042():
	a = 1
	while True:
		yield int("1"*a)
		a += 1

def A000043():
	a = 0
	while True:
		if sympy.isprime(2**a-1):
			yield a
		a += 1

def A000051():
	a = 0
	while True:
		yield 2**a+1
		a += 1

def A000059():
	a = 0
	while True:
		if sympy.isprime((2*a)**4+1):
			yield a
		a += 1

def A000062():
	a = 1
	while True:
		yield math.floor(a/(math.e-2))
		a += 1

def A000068():
	a = 0
	while True:
		if sympy.isprime(a**4 + 1):
			yield a
		a += 1

def A000069():
	a = 0
	while True:
		if str(bin(a)).count("1")%2 == 1:
			yield a
		a += 1

def A000079():
	a = 1
	while True:
		yield a**2
		a += 1

def A000093():
	a = 0
	while True:
		yield math.floor(a**(3/2))
		a += 1

def A000290():
	a = 0
	while True:
		if math.sqrt(a).is_integer():
			yield a
		a += 1

def A001969():
	a = 0
	while True:
		if str(bin(a)).count("1")%2 == 0:
			yield a
		a += 1

def A005408():
	a = 1
	while True:
		yield a
		a += 2

def A005843():
	a = 0
	while True:
		yield a
		a += 2
