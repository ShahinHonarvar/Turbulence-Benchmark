
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(18, 88):
        for j in range(i+37, i+61):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
