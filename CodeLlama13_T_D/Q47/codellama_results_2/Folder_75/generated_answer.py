
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 75):
        for j in range(23, 40):
            substr = string[i:j]
            if len(substr) == j - i and all(substr[::-1] == substr):
                palindromes.add(substr)
    return palindromes
