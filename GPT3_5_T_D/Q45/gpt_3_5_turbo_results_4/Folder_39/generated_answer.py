
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters
    from itertools import permutations

    substring = string[2:6]
    letters = ''.join([c.lower() for c in substring if c.isalpha()])
    pali_set = set()

    for perm in itertools.permutations(letters):
        perm = ''.join(perm)
        perm = perm.lower()
        if perm == perm[::-1] and len(perm) >= 3:
            pali_set.add(perm)
    
    return pali_set
