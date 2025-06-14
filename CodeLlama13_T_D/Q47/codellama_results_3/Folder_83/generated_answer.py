
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(75, 96):
        for j in range(i+7, i+10):
            substr = string[i:j]
            if len(substr) <= 9 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
