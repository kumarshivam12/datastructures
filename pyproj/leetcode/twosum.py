target = 6
d = {}
nums = [2, 3, 4]
for k, v in enumerate(nums):
    digit = target-v
    if digit in d:
        print([d[digit], k])
    else:
        d[v] = k
print(d)


t = 6
di = {}


def get_key(val):
    for key, value in di.items():
        if val == value:
            return key


l = [2, 3, 4]
for i, j in enumerate(l):
    diff = t-j
    if diff in di.values():
        print([get_key(diff),i ])
    else:
        di[i] = j
print(di)
