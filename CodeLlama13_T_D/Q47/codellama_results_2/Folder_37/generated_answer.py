
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 6):
        for j in range(10):
            substr = string[j:j+i]
            if substr == substr[::-1] and all(c.isalpha() for c in substr):
                palindromes.add(substr)
    return palindromes
