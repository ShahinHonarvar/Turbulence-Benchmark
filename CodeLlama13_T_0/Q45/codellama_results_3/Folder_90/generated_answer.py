
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 6):
        for j in range(i + 4, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
