
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(27, 96):
        for j in range(i+48, i+52):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
