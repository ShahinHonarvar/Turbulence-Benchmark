
def palindromes_between_indices(string):
    indices = range(6, 9)
    palindromes = set()
    for i in indices:
        for j in range(i + 1, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
