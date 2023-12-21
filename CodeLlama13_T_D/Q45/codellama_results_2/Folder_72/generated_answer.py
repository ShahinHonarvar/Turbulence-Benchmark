
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 7 + 1):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
