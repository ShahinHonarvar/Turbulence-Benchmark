
from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[:8]
    s_counter = Counter(s)
    palindromes_set = set()
    
    for perm in permutations(s):
        possible_word = "".join(perm)
        if possible_word == possible_word[::-1] and len(possible_word) >= 7:
            palindromes_set.add(possible_word)
    return palindromes_set
