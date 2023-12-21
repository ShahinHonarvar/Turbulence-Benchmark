
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(2, len(s) - 3):
        for j in range(i + 1, len(s) - 2):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
