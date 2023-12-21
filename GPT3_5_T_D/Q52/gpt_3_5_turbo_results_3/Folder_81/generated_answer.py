
def palindrome_of_length_n(string):
    n = 99
    lowercase_string = string.lower()
    palindromes = set()
    
    for i in range(len(lowercase_string) - n + 1):
        substring = lowercase_string[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
