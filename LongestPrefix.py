# This Problem is 14th problem in lettcode that name is Longest Common Prefix.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Given a string array strs, return the longest common prefix
# of the smallest string in strs.
# If there is no common prefix, return an empty string "".
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# I solve this in 1402/12/19

def longestCommonPrefix(strs: list[str]) -> str:
    strs = sorted(strs)
    s = 1
    iter = 0
    while iter < len(strs[0]) and s != 0 :
        letter = strs[0][iter]
        for i in range(1, len(strs)):
            if strs[i][iter] == letter:
                continue
            else:
                iter -= 1
                s = 0
                break
        iter += 1

    return strs[0][0:iter]

# Test Case
strs = ["ab", "a"]
# Output = ""
print(longestCommonPrefix(strs))


