
def palindromes_between_indices(string):
    indices = range(5, 8)
    palindromes = set()
    for i in indices:
        for j in indices:
            if i <= j:
                substr = string[i:j]
                if len(substr) >= 3 and substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
