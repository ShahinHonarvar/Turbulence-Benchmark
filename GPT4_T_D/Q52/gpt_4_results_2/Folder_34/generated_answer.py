
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i + 33, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and all(c.isalpha() for c in substr):
                results.add(substr)
    return results
