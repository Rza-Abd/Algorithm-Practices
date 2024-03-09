# This Problem is 13th problem in lettcode that name is Roman To Integer.
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# I do this at 1401/12/19


s = "MCMXCIV"
output = 1994

def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_list = [letter for letter in s]
    num = roman_dict[s_list[0]]
    print(s_list)
    for iter in range(1,len(s_list)):
        num += roman_dict[s_list[iter]]
        if roman_dict[s_list[iter]] > roman_dict[s_list[iter-1]] :
            num -= (2 * roman_dict[s_list[iter-1]])
        print(num)
    return num

print(romanToInt(s))