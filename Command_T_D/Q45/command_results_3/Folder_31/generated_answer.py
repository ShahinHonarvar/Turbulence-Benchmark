def palindromes_between_indices(s):
    letters = set(s.lower()[:8])
    return set(x[::-1] for x in ("".join(x) for x in itertools.permutations(letters)))
