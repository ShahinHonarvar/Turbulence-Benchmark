
def palindromes_between_indices(string):
    import itertools

    indices = range(4, 9)
    letters = [char for char in string if char.isalpha()]
    combinations = itertools.permutations(letters, len(indices))
    palindromes = set()

    for combination in combinations:
        word = ''.join(combination).lower()
        if word == word[::-1]:
            palindromes.add(word)

    return palindromes
