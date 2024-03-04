# This is 15th Problem in LeetCode
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    i = 0

    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1

        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum == 0:
                res.append([nums[i], nums[j], nums[k]])

                # Move j and k to the next distinct elements
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1

                j += 1
                k -= 1
            elif current_sum < 0:
                j += 1
            else:
                k -= 1

        # Move i to the next distinct element
        while i < len(nums) - 2 and nums[i] == nums[i + 1]:
            i += 1

        i += 1

    return res

# Test the code
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))