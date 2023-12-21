
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = 46
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
