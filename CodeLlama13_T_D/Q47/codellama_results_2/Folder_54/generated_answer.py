
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i+18, i+20):
            substr = string[i:j]
            if len(substr) >= 18 and len(substr) <= 19 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
