
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 75):
        for j in range(23, 40):
            substr = string[i:i+j]
            if len(substr) != len(set(substr)):
                continue
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
