
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 6 + 1):
        substr = string[i:i+6]
        if len(substr) < 6:
            break
        for j in range(0, len(substr)):
            substr_j = substr[:j]
            substr_rest = substr[j:]
            if substr_j == substr_rest[::-1]:
                palindromes.add(substr_j)
    return palindromes
