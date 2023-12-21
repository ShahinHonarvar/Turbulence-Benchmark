
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, len(string) - 4):
        for j in range(i + 1, len(string) - 3):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
