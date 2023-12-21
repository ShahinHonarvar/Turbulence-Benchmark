
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 8):
        for j in range(i+6, 8):
            substr = string[i:j]
            if len(substr) < 6:
                continue
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
