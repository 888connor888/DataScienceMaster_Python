def check_prime(n):
	x=1
	if n==2:
		return 1
	else:
		for i in range(2,n):
			if n%i==0:
				x=0
				break
			else:
				x=1
		return x		
				
		

#num=int(input('Enter the no. to check:'))
#temp=check_prime(num)
#if temp==1:
#	print('The number is prime.')
#else:
#	print('the number is not a prime number')
def print_prime(N):
	for i in range(2,N+1):
		temp=check_prime(i)
		if temp==1:
			print(i)

N=int(input('Enter the number:'))
print_prime(N)		

			





			