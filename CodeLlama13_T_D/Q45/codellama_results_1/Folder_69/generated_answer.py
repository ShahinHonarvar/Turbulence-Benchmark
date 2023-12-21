
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 3):
        substr = string[i:i+4]
        if len(substr) < 4:
            continue
        rev_substr = substr[::-1]
        if substr == rev_substr and all(c.isalpha() for c in substr):
            palindromes.add(substr)
    return palindromes
