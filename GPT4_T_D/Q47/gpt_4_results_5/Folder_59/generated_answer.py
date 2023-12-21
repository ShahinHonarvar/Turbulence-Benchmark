
def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[0:101]
    result = set()
    for l in range(3, 16):
        for i in range(len(s) - l + 1):
            substring = s[i:i + l]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
