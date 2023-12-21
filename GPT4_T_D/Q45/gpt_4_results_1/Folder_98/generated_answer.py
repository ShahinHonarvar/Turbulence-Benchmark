
import itertools

def palindromes_between_indices(s):
    subset = s[3:6]
    all_list = []
    for l in range(4, len(subset)+1):
        all_list.extend([''.join(p).lower() for p in itertools.permutations(subset, l)])

    palindromes = set([word for word in all_list if word == word[::-1]])
    return palindromes
