def check_prime(n):
  x=1
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    for i in range(2,n):
      if n%i==0:
        x=0
        break
      else:
        x=1
  return x  

				
def generate_prime(l,h):
  my_str=""
  for i in range(l,h+1):
    if check_prime(i):
      my_str += '{} '.format(i)
  return my_str    

t=int(input())
