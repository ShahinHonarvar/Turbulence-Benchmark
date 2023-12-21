
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set() 
    for len_sub in range(89, len(s) + 1):
        for start in range(len(s) - len_sub + 1):
            substr = s[start:start+len_sub]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
