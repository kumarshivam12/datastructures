from collections import Counter
from sys import stdin, stdout
'''
#lines=list(map(int, stdin.readline().split()))
#print(lines)
#print(Counter(lines))
my_list=[1, 1, 2, 2, 3, 3, 3, 3, 44, 4, 4, 4, 4, 55, 55, 66, 6, 6, 77, 7, 7, 8, 99, 9, 7, 7, 6, 5, 4, 3]
freq = {} 
for item in my_list: 
    if (item in freq): 
        freq[item] += 1
        #print(freq)
    else: 
        freq[item] = 1
        

for key, value in freq.items(): 
    #print ("% d : % d"%(key, value))

keys = ['red', 'green', 'blue']
d=dict.fromkeys(keys,keys.index)
d1={k: v for k,v in enumerate(keys)}
print(d1)

'''
s = [[int(i) for i in input().split(' ')] for j in range(3)]
n = [s[i][j] for i in range(3) for j in range(3)]    
all_n = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

allsum = []
for l in all_n:
    allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))
print(min(allsum))










    