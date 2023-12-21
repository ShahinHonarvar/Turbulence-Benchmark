
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i + 18, i + 37):
            substr = string[i:j]
            if len(substr) % 2 == 0:
                continue
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
