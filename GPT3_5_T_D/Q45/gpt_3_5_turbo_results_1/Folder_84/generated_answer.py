
def palindromes_between_indices(string):
    import itertools
    import re

    letters = ''.join(re.findall('[A-Za-z]', string[4:10]))
    palindromes = set()

    for comb in itertools.permutations(letters, len(letters)):
        word = ''.join(comb)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word)

    return palindromes
