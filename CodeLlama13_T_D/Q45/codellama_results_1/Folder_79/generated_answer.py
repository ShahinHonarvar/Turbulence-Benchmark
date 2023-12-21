
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i+2, 8):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
