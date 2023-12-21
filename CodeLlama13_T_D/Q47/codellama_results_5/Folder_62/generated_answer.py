
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 87+1):
        for j in range(52, 56+1):
            substr = string[i:i+j]
            if len(substr) <= 1 or substr[0] == substr[-1]:
                continue
            if all(c.isalpha() and c.islower() for c in substr):
                palindromes.add(substr)
    return palindromes
