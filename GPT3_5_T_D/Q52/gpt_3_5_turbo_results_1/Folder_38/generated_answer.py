
def palindrome_of_length_n(string):
    set_of_palindromes = set()
    n = 38
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            set_of_palindromes.add(substring)
    
    return set_of_palindromes
