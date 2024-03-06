# This Problem is 16th problem in lettcode that name is 3Sum Closest
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# mapping of digit to letters (just like on the telephone buttons).
# like this: digits="23" return ['ad','ae','af','bd','be','bf','cd','ce','cf']


# I write this answer and get accept submition:
def letterCombinations(digits: str) -> list[str]:

    letter_dict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i']
                        , '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                            '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}

    target_dict = []
    letters = []

    for l in digits:
        target_dict.append(letter_dict[l])

    i1, i2, i3, i4, i5, i6, i7, i8 = '' , '', '', '', '', '', '', ''

    for i1 in target_dict[0]:
        if len(target_dict) == 1:
            letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8) 
            continue
        else:
            for i2 in target_dict[1]:
                if len(target_dict) == 2:
                    letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                    continue
                else:
                    for i3 in target_dict[2]:
                        if len(target_dict) == 3:
                            letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                            continue
                        else:
                            for i4 in target_dict[3]:
                                if len(target_dict) == 4:
                                    letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                    continue
                                else:
                                    for i5 in target_dict[4]:
                                        if len(target_dict) == 5:
                                            letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                            continue
                                        else:
                                            for i6 in target_dict[5]:
                                                if len(target_dict) == 6:
                                                    letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                                    continue
                                                else:
                                                    for i7 in target_dict[6]:
                                                        if len(target_dict) == 7:
                                                            letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                                            continue
                                                        else:
                                                            for i8 in target_dict[7]:
                                                                letters.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)

    return letters

# but the best answers is :
def letterCombinations1(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    combinations = [""]

    for digit in digits:
        new_combinations = []
        for combination in combinations:
            for letter in phone_map[digit]:
                new_combinations.append(combination + letter)
        combinations = new_combinations

    return combinations

# another one is :
def letterCombinations2(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    backtrack("", digits)
    return output