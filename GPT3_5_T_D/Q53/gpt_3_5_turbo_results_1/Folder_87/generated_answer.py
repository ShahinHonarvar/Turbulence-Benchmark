
def palindrome_of_length_at_least_n(string):
    import re
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i+17, len(string)):
            substring = string[i:j+1]
            if re.match("^[a-zA-Z]+$", substring) and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
