
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(len(s) - 5):
        substr = s[i:i+6]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
