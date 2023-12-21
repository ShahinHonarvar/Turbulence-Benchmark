
def palindromes_between_indices(s):
    return {p for p in [''.join(c) for c in itertools.permutations(s[1:8])] if p == p[::-1]}
