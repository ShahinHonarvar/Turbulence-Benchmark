
def palindromes_between_indices(string):
    import itertools

    letters = [ch for ch in string[2:7] if ch.isalpha()]
    perms = {"".join(permutation).lower() for permutation in itertools.permutations(letters)}
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 4}

    return palindromes
