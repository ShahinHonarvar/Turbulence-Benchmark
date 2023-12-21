
def palindromes_between_indices(s):
    from itertools import permutations

    # Extract required string section
    s = s[1:5].lower()

    # Generate all permutations
    perms = [''.join(p) for p in permutations(s) if len(p) >= 3]

    # Only keep permutations that are palindromes
    pals = set(p for p in perms if p == p[::-1])

    return pals
