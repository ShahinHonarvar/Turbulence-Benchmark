
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 181, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 181 and all(c.isalpha() for c in substr):
                if substr == substr[::-1]:
                    result.add(substr)
    return result
