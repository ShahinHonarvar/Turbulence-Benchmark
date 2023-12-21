
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(51):
        for j in range(50, 101):
            substring = string[:i]
            if substring == substring[::-1] and substring.isalpha() and len(substring) == j:
                palindromes.add(substring)
    return palindromes
