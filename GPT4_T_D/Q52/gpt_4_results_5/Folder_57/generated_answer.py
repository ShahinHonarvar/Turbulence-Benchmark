
def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    if len(s) < 92:
        return result_set
    for i in range(len(s) - 91):
        substr = s[i:i+92]
        if substr.isalpha() and substr == substr[::-1]:
            result_set.add(substr)
    return result_set
