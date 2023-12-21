
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 15 + 1):
        substring = string[i:i+15]
        if len(substring) == 15 and all([c.isalpha() for c in substring]):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
