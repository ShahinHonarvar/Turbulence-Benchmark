
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 223 + 1):
        substr = s[i:i+223]
        if substr == substr[::-1] and substr.isalpha():
            result.add(substr)
    return result
