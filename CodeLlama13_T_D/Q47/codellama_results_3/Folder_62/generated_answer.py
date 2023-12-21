
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 87+1):
        for j in range(52, 56+1):
            substr = string[i:i+j]
            if len(substr) == j and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
