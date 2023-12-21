
def palindrome_of_length_at_least_n(s):
    import re
    s = s.lower()
    s = re.sub(r'\W+', '', s)
    results = set()
    for i in range(len(s)):
        for j in range(i + 33, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                results.add(substr)
    return results
