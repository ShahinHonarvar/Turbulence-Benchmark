
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 3):
        substr = string[i:i+4]
        if len(substr) < 4:
            continue
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
