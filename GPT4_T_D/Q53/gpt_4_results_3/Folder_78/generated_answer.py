
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    n = 96
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
