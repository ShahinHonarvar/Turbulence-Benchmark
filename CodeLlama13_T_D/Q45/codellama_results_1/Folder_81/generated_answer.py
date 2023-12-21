
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(7):
        for j in range(i, 7):
            substr = s[i:j+1]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
