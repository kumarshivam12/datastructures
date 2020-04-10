'''
from sys import stdin
n,a = input(),list(map(int,stdin.readline().split()))
def pick(a):
    print(max(a.count(x)+a.count(x+1) for x in set(a)))
pick(a)
import string
def alphabet_position(text):
        alphabeths = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}
        print(alphabeths)
        #return " ".join(str(alphabeths.get(char)) for char in text.lower() if char in alphabeths.keys())    
alphabet_position('shivam')
'''
d = {L: i for i, L in enumerate('abcdefghijklmnopqrstuvwxyz', 1)}
print(d)
new='zaba'
l=[19, 20, 21, 22, 23, 24, 25, 26,13, 14, 15, 16, 17, 18,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
p=[]
for i in new:
    pos=d.get(i)
    p.append(l[pos-1])
print(p)    