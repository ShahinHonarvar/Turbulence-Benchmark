
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 5):
        substr = string[i:i+6]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
