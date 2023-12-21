
def palindrome_of_length_n(s):
    palindrome_set = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                palindrome_set.add(substring)
    return palindrome_set
