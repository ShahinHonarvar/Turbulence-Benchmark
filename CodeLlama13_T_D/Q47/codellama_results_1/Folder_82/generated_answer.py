
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 301):
        for j in range(len(string) - i + 1):
            substr = string[j:j+i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
