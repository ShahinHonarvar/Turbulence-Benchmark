
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 68, len(s) + 1):
            substr = s[start:end]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result
