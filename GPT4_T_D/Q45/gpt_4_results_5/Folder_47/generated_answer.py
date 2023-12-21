
import itertools

def palindromes_between_indices(s):
    s_substring = s[3:8].lower()
    s_substring_letters = ''.join(ch for ch in s_substring if ch.isalpha())
    permutations = set(''.join(p) for p in itertools.permutations(s_substring_letters))
    return set(p for p in permutations if len(p) >= 5 and p == p[::-1])
