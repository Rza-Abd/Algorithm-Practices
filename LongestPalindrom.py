
def longestpalindrom(s: str) -> str:
    def palindrom(word: str) -> bool:
        if word == word[::-1]:
            return True
        return False
    if not s:
        return ""
    if len(s) == 1:
        return s
    max_len = 0
    max_word = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            word = s[i:j]
            if palindrom(word) and len(word) > max_len:
                max_len = len(word)
                max_word = word
    return max_word

print(longestpalindrom("babad"))