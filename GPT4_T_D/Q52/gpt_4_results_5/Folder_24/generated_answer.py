
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 29, length + 1):
            substr = s[start:end]
            if substr == substr[::-1] and all(ch.isalpha() for ch in substr):
                result.add(substr)
    return result
