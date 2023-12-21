
def palindrome_of_length_at_least_n(string):
    string = ''.join(c for c in string if c.isalpha())
    string = string.lower()
    n = len(string)
    palindromes = set()
    
    for i in range(n):
        for j in range(i+138, n+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
