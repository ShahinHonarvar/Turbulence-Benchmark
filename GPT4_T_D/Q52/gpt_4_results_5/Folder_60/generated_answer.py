
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 87):
        substr = s[i:i+88]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result
