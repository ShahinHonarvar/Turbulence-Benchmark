
import itertools

def palindromes_between_indices(s):
    s = s[5:10].lower()
    all_combinations = itertools.permutations(s)
    all_strings = set(''.join(ch) for ch in all_combinations)
    palindromes = set(filter(lambda x: x == x[::-1] and len(x) >= 6, all_strings))
    return palindromes
