
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    s = ''.join(c for c in s if c.isalpha())
    for i in range(len(s)):
        for j in range(i + 73, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
