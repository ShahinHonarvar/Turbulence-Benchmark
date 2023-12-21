
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    palindrome_set = set()
    for i in range(6, len(s)+1):
        for p in permutations(s, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindrome_set.add(p_str)
    return palindrome_set
