
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    results = set()
    for i in range(len(s)):
        for j in range(i + 23, len(s) + 1):
            if j - i == 23:
                substring = s[i:j]
                if substring == substring[::-1]:
                    results.add(substring)
    return results
