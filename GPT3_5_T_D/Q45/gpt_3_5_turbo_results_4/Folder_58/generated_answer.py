
def palindromes_between_indices(string):
    import itertools
    import string

    letters = set(string.ascii_lowercase)
    indices = range(7)

    palindromes = set()

    for comb in itertools.combinations(indices, 6):
        substr = ''
        for i in comb:
            if string[i].lower() not in letters:
                substr = ''
                break
            substr += string[i].lower()
        if substr:
            if substr == substr[::-1]:
                palindromes.add(substr)

    return palindromes
