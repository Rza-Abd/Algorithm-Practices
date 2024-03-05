# This Problem is 16th problem in lettcode that name is 3Sum Closest
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# I do this at 1401/12/15

def threeSumClosest(nums, target):
  
    nums.sort()
    n = len(nums)
    best = sum(nums[:3])

    for i in range(n):
        lo = i+1
        hi = n-1
        while lo < hi:
        current_sum = nums[i] + nums[lo] + nums[hi]
        if abs(current_sum - target) < abs(best - target):
            best = current_sum
        if current_sum < target:
            lo += 1  
        else: 
            hi -= 1

    return best


# Test the code
nums = [1,1,1,0]
target = -100
print(threeSumClosest(nums, target))