
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 299 + 1):
        for j in range(i, min(i + 10 - 1, len(string)) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
