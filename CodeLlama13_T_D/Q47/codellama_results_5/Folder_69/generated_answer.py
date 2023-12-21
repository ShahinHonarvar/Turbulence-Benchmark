
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 96 + 1):
        for j in range(i, 96 + 1):
            substr = string[i:j]
            if len(substr) >= 45 and len(substr) <= 52 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
