
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 7):
        for j in range(i+2, 7):
            substr = string[i:j]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
