# This Problem is 16th problem in lettcode that name is 3Sum Closest
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# I do this at 1401/12/15

def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    min_diff = float('inf')
    res = 0
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < min_diff:
                min_diff = abs(s - target)
                res = s
            if s < target:
                l += 1
            else:
                r -= 1
    return s

# Test the code
nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))