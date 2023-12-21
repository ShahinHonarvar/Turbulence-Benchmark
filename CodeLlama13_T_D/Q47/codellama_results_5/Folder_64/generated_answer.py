
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(4, 6):
        for j in range(8 - i):
            substr = string[j:j + i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
