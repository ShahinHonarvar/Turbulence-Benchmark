
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 141
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result
