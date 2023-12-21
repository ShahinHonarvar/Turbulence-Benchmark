
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 6):
        for j in range(i + 2, 6):
            substr = string[i:j]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
