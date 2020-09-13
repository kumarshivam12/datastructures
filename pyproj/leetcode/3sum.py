t = 0
nums = [-1, 0, 1, 2, -1, -4]
n = len(nums)
res = []
nums.sort()
for i, v in enumerate(nums):
    if i > 0 and v == nums[i-1]:
        continue
    l, r = i+1, len(nums)-1
    while l < r:
        threesome = v + nums[l]+nums[r]
        if threesome > 0:
            r -= 1
        elif threesome < 0:
            l += 1
        else:
            res.append([v, nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l-1] and l < r:
                l += 1
print(res)