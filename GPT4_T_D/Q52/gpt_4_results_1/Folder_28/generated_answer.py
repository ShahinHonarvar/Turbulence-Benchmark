
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)-42):
        substr = s[i:i+43]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result
