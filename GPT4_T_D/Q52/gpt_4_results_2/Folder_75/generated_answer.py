
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+80, len(s)+1):
            substr = s[i:j]
            if len(substr) == 80:
                if all(c.isalpha() for c in substr) and substr == substr[::-1]:
                    results.add(substr)
    return results
