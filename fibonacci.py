n=int(input())
#n is the no. of elements you need in the series
a=[]
fib1=-1
fib2=1
sum=0
for i in range(n):
    sum=fib1+fib2
    a.append(sum)
    fib1=fib2
    fib2=sum
for i in a:
    print(i,end=" ")
