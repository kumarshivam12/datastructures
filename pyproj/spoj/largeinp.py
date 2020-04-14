from sys import stdin
count=0
n,k=(stdin.readline().split())
n=int(n)
k=int(k)
for i in range(n):
    t=int(stdin.readline())
    if t%k==0:
        count+=1
print(count)

