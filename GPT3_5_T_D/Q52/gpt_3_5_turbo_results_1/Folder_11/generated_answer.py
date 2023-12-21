
def palindrome_of_length_n(string):
    n = 77
    palindromes = set()
    string = string.lower()
    
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
