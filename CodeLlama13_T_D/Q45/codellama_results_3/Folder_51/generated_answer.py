
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 6):
        for j in range(i + 1, len(string) - (i - 1)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
