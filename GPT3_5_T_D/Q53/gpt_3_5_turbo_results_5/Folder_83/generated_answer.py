
def palindrome_of_length_at_least_n(string):
    from itertools import combinations
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i + 60, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
