
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 56):
        for j in range(3, 8):
            substr = string[i:i+j]
            if len(substr) == j and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
