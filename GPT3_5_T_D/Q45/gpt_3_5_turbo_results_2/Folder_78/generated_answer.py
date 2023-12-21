
def palindromes_between_indices(string):
    import itertools
    import re

    start_index = 6
    end_index = 8

    letters = re.findall('[a-zA-Z]', string[start_index:end_index + 1])
    if not letters:
        return set()

    letters = ''.join(letters).lower()
    palindromes = set()

    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
