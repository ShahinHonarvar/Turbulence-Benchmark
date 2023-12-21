
def palindromes_between_indices(string):
    import itertools

    english_letters = [char for char in string if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]

    comb = itertools.combinations(english_letters, 7)
    palindromes = set()

    for c in comb:
        if c == c[::-1]:
            palindromes.add(''.join(c))

    return palindromes
