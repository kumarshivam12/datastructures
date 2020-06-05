n, k = map(int, input().split())
total = []
for _ in range(k):
  d = int(input())
  A = list(map(int, input().split()))
print(A)
for a in A:
    total.append(a)
print(total)
ans = n - len(set(total))
print(ans)