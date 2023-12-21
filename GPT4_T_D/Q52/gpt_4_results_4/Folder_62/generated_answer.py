
def palindrome_of_length_n(s):
    s = s.lower()
    n = 188
    result = set()
    for i in range(len(s)):
        if i + n > len(s):
            break
        substr = s[i:i+n]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result
