
def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    for i in range(len(s) - 392 + 1):
        substr = s[i:i+392]
        if substr == substr[::-1]: # check if palindrome
            results.add(substr)
    return results
