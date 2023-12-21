
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(63, 71):
        for j in range(i+4, i+6):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
