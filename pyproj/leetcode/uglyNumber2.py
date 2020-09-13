from sys import stdin
n = int(stdin.readline())


def nthUglyNumber(n):
    l1 = [1]
    for i in range(1, 1691):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            l1.append(i)
            if len(l1) == n:
                break
        if len(l1) == n:
            break
    return l1[(len(l1)-1)]


print(nthUglyNumber(n))
