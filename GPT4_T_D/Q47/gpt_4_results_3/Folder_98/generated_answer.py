
def palindromes_of_specific_lengths(s):
    import re
    s = s[:21].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 5, min(i + 81, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
