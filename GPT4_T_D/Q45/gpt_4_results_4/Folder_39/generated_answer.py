
from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:6].lower()
    string_comb = [''.join(p) for p in permutations(sub_string)]
    return {word for word in string_comb if len(word) >= 3 and word == word[::-1]}
