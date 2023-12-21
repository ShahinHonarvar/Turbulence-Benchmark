
from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7]
    s = s.lower()
    possible_palindromes = set()

    for word_length in range(4, len(s) + 1):
        for perm in permutations(s, word_length):
            word = ''.join(perm)
            if word == word[::-1]:
                possible_palindromes.add(word)

    return possible_palindromes
