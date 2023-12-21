
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(4, 10):
        for j in range(i+1, 10):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
