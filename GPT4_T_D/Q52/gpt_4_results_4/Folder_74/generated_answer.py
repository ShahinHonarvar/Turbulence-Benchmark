
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 95):
        substr = s[i:i+96]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result
