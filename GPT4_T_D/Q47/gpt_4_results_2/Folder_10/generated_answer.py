
def palindromes_of_specific_lengths(s):
    s = s[16:61]
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+16, min(i+40, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
