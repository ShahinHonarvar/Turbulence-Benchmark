
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(104, 123 + 1):
        for j in range(119, 256 + 1):
            substr = string[j:j+i]
            if len(substr) == i and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
