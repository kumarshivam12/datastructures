from collections import Counter
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
freq=dict(Counter(l))
ans=list(freq.values())
print(len(ans))