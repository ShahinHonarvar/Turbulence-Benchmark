
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i+41, i+78):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
