
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_string = s[:7]
    potential_palindromes = set()

    for i in range(6, len(sub_string) + 1):
        for tpl in list(permutations(sub_string, i)):
            potential_word = ''.join(tpl)
            if potential_word == potential_word[::-1]:
                potential_palindromes.add(potential_word)

    return potential_palindromes
