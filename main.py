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

def A005843():
	a = 0
	while True:
		yield a
		a += 2
