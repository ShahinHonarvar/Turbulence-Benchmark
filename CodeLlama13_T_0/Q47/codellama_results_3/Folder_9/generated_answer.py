
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(50, 61):
        for j in range(301 - i):
            substr = string[j:j + i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
