
def palindromes_between_indices(string):
    indices = set()
    for i in range(3, 7):
        indices |= {i - j for j in range(4)}
    palindromes = set()
    for i in indices:
        for j in range(i + 1, len(string) - 2):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
