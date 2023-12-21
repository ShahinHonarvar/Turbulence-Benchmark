
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+27, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and all(c.isalpha() for c in substring):
                results.add(substring)
    return results
