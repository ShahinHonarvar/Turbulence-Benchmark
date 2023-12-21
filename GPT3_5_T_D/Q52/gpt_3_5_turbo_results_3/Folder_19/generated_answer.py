
def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    length = len(string)
    
    for i in range(length - 66):
        substring = string[i:i+67]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
