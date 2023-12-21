
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(103, 276+1):
        for j in range(i+99, i+170):
            substr = string[i:j]
            if len(substr) > 1 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
