
import itertools

def palindromes_between_indices(s):
    s = s[3:9].lower()
    palindromes = set()
    for i in range(7, len(s) + 1):
        combinations = itertools.permutations(s, i)
        for combination in combinations:
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
