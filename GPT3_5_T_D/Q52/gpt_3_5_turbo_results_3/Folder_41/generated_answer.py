
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    n = len(string)
    
    if n < 60:
        return palindromes
    
    for i in range(n-59):
        substring = string[i:i+60]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
