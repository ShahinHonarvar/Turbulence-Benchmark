
def palindrome_of_length_at_least_n(string):
    length = len(string)
    if length < 72:
        return set()
    
    lowercase_string = string.lower()
    palindromes = set()
    
    for i in range(0, length - 69):
        substring = lowercase_string[i:i + 70]
        if substring == substring[::-1]:
            palindromes.add(substring)
            
    return palindromes
