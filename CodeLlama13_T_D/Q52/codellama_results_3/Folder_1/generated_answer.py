
def palindrome_of_length_n(string, n):
    if len(string) < n:
        return set()
    
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if is_palindrome(substr):
            palindromes.add(substr)
    
    return palindromes
