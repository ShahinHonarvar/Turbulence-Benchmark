
def palindrome_of_length_at_least_n(string):
    n = 22
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
