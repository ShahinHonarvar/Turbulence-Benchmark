
import itertools

def palindromes_between_indices(s):
    s = s[7:10].lower()
    palindromes = set()

    for permutation in itertools.permutations(s):
        word = "".join(permutation)
        if len(word) > 2 and word == word[::-1]:
            palindromes.add(word)

    return palindromes
