
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(8):
        for j in range(i, 8):
            substr = string[i:j+1]
            if len(substr) >= 4 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
