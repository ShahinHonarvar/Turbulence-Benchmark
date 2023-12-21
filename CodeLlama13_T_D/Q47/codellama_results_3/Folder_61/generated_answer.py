
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(20, 31):
        for j in range(0, len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1] and all(c.isalpha() for c in substr):
                palindromes.add(substr)
    return palindromes
