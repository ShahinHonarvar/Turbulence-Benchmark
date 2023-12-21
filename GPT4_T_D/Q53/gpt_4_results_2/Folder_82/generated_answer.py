
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub('[^a-z]+', '', s.lower())
    str_len = len(s)
    palindromes = set()
    for length in range(72, str_len + 1):
        for i in range(str_len - length + 1):
            substr = s[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
