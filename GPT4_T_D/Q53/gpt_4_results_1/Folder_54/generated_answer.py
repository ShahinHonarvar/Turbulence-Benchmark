
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    result = set()
    for i in range(len(s)):
        for j in range(i + 74, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result
