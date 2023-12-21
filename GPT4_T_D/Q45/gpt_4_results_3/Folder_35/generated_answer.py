
import itertools

def palindromes_between_indices(s):
    sub_str = s[2:5].lower()
    letter_arrangements = set([''.join(p) for p in itertools.permutations(sub_str)])
    return set([p for p in letter_arrangements if p == p[::-1] and len(p) >= 4])
