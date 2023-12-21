
def palindromes_between_indices(string):
    import itertools

    letters = [c.lower() for c in string[6:10] if c.isalpha()]
    combinations = set(itertools.permutations(letters))

    palindromes = set()
    for combination in combinations:
        word = ''.join(combination)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)

    return palindromes
