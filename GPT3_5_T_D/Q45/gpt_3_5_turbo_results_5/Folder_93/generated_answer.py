
def palindromes_between_indices(string):
    import itertools
    import re

    symbols = re.findall(r'[a-zA-Z]', string)
    if len(symbols) < 6:
        return set()

    symbols = set(symbols[2:8])
    if len(symbols) < 6:
        return set()

    palindromes = set()
    for perm in itertools.permutations(symbols, 6):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word.lower())

    return palindromes
