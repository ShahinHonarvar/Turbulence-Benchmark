
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(3, 9):
        for j in range(i+1, 10):
            substr = s[i:j]
            if len(substr) >= 4 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
