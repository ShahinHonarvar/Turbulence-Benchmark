
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(17, 96):
        for j in range(i+13, i+50):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
