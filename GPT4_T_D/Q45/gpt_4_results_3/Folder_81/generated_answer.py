
from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:7].lower()
    palindrome_set = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            p_word = "".join(p)
            if p_word == p_word[::-1]:
                palindrome_set.add(p_word)
    return palindrome_set
