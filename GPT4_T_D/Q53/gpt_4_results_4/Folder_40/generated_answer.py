
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and substring.isalpha() and len(substring) >= 3:
                results.add(substring)
    return results
