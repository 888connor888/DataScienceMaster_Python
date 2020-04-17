n=int(input())
for i in range(n+1,1,-1):
    my_str=""
    for j in range(1,i):
        my_str+="{} ".format(j)
    if i!=n+1: 
        for k in range(2*(n-i+1)-1):
            my_str+="* "
    print(my_str)    