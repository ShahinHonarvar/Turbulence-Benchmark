
def palindromes_between_indices(string):
    import itertools
    import re

    substrings = set()
    for i in range(1, 9):
        substrings.update(set(itertools.permutations(string[i:9], 8-i+1)))

    palindromes = set()
    for substring in substrings:
        if substring[::-1].lower() == substring.lower():
            palindromes.add(''.join(substring))

    return palindromes
