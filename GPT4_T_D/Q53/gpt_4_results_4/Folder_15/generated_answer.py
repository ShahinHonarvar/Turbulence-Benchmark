
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for length in range(4, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start+length]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result
