
def palindrome_of_length_at_least_n(string):
    import re
    
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 61):
        substring = string[i:i+62]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
