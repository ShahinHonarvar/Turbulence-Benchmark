
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 80):
        for j in range(i + 1, 80):
            substr = string[i:j]
            if len(substr) >= 35 and len(substr) <= 41 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
