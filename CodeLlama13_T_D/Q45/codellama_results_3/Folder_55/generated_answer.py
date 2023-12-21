
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 2):
        substr = string[i:i + 3]
        if substr[0] == substr[-1]:
            palindromes.add(substr)
    return palindromes
