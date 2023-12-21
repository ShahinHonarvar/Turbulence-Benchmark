
import itertools

def palindromes_between_indices(s):
    s = s[6:10].lower()
    perms = set(itertools.permutations(s))
    palindromes = set()

    for perm in perms:
        tmp = ''.join(perm)
        if len(tmp) >= 5 and tmp == tmp[::-1]:
            palindromes.add(tmp)

    return palindromes
