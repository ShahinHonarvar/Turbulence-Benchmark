
def palindromes_between_indices(string):
    import itertools
    import re

    letters = re.findall(r'[a-zA-Z]', string)
    letters = [c.lower() for c in letters]

    palindromes = set()
    for chars in itertools.permutations(letters, r=5):
        word = ''.join(chars)
        if word == word[::-1]:
            palindromes.add(word)

    return palindromes
