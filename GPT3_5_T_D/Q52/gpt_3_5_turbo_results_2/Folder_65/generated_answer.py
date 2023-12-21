
def palindrome_of_length_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    
    for i in range(length - 34):
        substring = string[i:i+35]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
