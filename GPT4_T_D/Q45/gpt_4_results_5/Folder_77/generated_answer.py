
from itertools import permutations

def palindromes_between_indices(text):
    subset_str = text[4:7].lower()
    palindromes = set()

    # create permutations of length at least 4
    for i in range(4, len(subset_str)+1):
        perm = set([''.join(p) for p in permutations(subset_str, i)])

        # if a permutation is a palindrome, add to set
        for word in perm:
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
