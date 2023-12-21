
def palindrome_of_length_n(string):
    palindromes = set()
    length = 279
    
    string = string.lower()  # Convert to lowercase for case-insensitive comparison
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
