
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    
    for i in range(length - 37):
        substring = string[i:i+38]
        
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
