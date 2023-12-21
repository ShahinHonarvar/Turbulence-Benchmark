
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(36, 92 + 1):
        for j in range(i + 10 - 1, i + 35 + 1):
            if j >= len(string):
                break
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
