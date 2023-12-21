
def palindromes_between_indices(string):
    import itertools
    
    substring = string[6:10].lower()
    perm = set(itertools.permutations(substring))

    palindromes = set()
    for p in perm:
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)

    return palindromes
