
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(5, 9):
        for j in range(i+2, len(string)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
