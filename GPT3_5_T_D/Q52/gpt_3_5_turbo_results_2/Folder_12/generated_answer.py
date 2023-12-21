
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)-22):
        substring = string[i:i+23]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
