from sys import stdin
r=int(stdin.readline())
def reverse(n):
    rev=str(n)[::-1]
    return int(rev)
for i in range(r):
    a,b=(input().split())
    a=reverse(a)
    b=reverse(b)
    res=reverse(a+b)
    print(res)