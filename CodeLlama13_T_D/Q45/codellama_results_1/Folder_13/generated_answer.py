
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 9 + 1):
        for j in range(i + 4, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
