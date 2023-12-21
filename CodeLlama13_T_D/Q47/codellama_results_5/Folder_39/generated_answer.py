
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i+49, i+54):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
