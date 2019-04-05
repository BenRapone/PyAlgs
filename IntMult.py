

def KaratMult(x,y):
	if len(str(x)) < 3 or len(str(y)) < 3:
		return x*y

	n = max(len(str(x)),len(str(y))) // 2

	a = x // 10**(n)
	b = x % 10**(n)
	c = y // 10**(n)
	d = y % 10**(n)

	v1 = KaratMult(a,c)
	v2 = KaratMult(b,d)
	v3 = KaratMult(a+b,c+d)

	return 10**(n*2)*v1+10**(n)*(v3-v2-v1)+v2


##### Tests
# from random import randint
# n = 2**8
# m = 2**15
# for i in range(0,m):
# 	x = randint(10**n,10**(n+1)-1)
# 	y = randint(10**n,10**(n+1)-1)
# 	# print(KaratMult(x,y))
# 	# print(x*y)
# 	if x*y != KaratMult(x,y):
# 		print(x,y)
# 		quit()
	



