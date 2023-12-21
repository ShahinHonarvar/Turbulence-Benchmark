
def palindromes_between_indices(string):
    import itertools
    english_letters = [char.lower() for char in string if char.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(english_letters, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes
