
def palindrome_of_length_n(s):
    s = s.lower()
    n = 16
    palindromes = set()
    for i in range(len(s)-n+1):
        substr = s[i:i+n]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
