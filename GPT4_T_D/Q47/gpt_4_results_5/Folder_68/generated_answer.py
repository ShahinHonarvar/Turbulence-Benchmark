
def palindromes_of_specific_lengths(s):
    import re
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    s = s[0:51]
    result = set()
    for i in range(0, len(s)):
        for j in range(i + 50, min(i + 101, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
