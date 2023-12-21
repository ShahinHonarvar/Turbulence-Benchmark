
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 6):
        substr = string[i:i+7]
        if len(substr) < 7:
            continue
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
