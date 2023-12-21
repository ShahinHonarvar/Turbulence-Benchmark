
from itertools import permutations

def palindromes_between_indices(str):
    sub_str = str[2:8].lower()
    palindrome_set = set()
    for i in range(3, len(sub_str)+1):
        perms = permutations(sub_str, i)
        for p in perms:
            p = ''.join(p)
            if p == p[::-1]:
                palindrome_set.add(p)
    return palindrome_set
