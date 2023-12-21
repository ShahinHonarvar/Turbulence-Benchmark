
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 475, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                result.add(substring)
    return result
