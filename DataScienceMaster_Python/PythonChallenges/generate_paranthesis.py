def generate_paranthesis(openB,closeB,n,s=[]):
	# base case
	if closeB==n:
		print(''.join(s))
		return
	else:
	  if openB>closeB:
		   s.append(')')
		   generate_paranthesis(openB,closeB+1,n,s)
		   s.pop()
	  if openB<n:
		   s.append('(')
		   generate_paranthesis(openB+1,closeB,n,s)
		   s.pop()
	return		

n=int(input())
generate_paranthesis(0,0,n)