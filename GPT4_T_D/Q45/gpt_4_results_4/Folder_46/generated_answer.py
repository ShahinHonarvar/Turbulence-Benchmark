
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    results = set()
    letter_set = set(s)
    for letter in letter_set:
        l_count = s.count(letter)
        if l_count >= 3:
            for p in permutations(s, l_count*2):
                chunk = ''.join(p)
                if chunk == chunk[::-1]:
                    results.add(chunk)
    return results
