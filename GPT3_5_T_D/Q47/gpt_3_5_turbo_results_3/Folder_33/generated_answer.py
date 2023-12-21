
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(103, 159):
        for start in range(130, 296 - length + 1):
            substring = string[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
