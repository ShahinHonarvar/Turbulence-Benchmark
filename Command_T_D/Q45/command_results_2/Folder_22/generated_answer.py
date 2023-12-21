def palindromes_between_indices(s):
    return set(a[5:-6] for a in ("".join(a) for a in zip(*[iter(s)])))
