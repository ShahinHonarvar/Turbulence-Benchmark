
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(29, 97):
        for j in range(i+12, i+18+1):
            substr = string[i:j]
            if len(substr) % 2 == 0 and substr.lower() == substr[::-1]:
                palindromes.add(substr)
    return palindromes
