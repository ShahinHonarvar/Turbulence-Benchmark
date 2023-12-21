
def palindromes_between_indices(string):
    import itertools
    import re

    letters = re.findall(r'[a-zA-Z]', string.lower())
    letters = letters[4:8]

    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)

    return palindromes
