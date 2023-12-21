
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 71 + 1):
        for j in range(i, min(len(string), 71) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
