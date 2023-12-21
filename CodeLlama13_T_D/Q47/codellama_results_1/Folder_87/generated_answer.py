
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 93 + 1):
        for j in range(i, min(i + 54 - 34 + 1, len(string)) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
