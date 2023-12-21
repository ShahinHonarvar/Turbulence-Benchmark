
def palindromes_between_indices(string):
    indices = range(2, 6)
    palindromes = set()
    for i in indices:
        for j in indices:
            if j < i:
                continue
            substr = string[i:j]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
