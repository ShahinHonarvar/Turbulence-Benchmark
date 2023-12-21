
def palindrome_of_length_n(string):
    palindromes = set()
    n = 28
    string = ''.join(filter(str.isalpha, string)).lower()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
