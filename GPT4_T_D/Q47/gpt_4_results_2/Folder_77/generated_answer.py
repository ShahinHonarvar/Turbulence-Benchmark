
def palindromes_of_specific_lengths(s):
    import re
    s = s[103:277]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 100, min(start + 170, len(s))):
            substring = s[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result
