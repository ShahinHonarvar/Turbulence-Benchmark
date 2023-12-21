
def palindromes_between_indices(string):
    import itertools
    import re

    letters = re.findall('[a-zA-Z]', string[3:8])
    letter_combinations = set(itertools.permutations(letters, len(letters)))

    palindromes = set()
    for combination in letter_combinations:
        word = ''.join(list(combination)).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)

    return palindromes
