
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 301):
        for j in range(i, 301):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
