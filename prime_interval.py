# Q..Write a python program to print all prime numbers in an interval??

for n in range(5,21):
    for i in range(2,n+1):
        if n%i==0:
            break
    if i==n:
        print(n,end=" ")
