
def palindromes_between_indices(string):
    import itertools

    english_letters = [c.lower() for c in string if c.isalpha()]
    english_letters_set = set(english_letters)
    palindromes = set()

    for length in range(3, 7):
        permutations = itertools.permutations(english_letters_set, length)
        for perm in permutations:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
