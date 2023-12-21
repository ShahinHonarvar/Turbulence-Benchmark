
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(24, 97 + 1):
        for j in range(i, min(i + 36, len(string))):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
