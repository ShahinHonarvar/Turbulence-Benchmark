
def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(130, 296):
        for j in range(103, 159):
            substring = string[i:i+j]
            if len(substring) == j and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
