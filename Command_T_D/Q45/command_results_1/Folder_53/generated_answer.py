def palindromes_between_indices(s):
    return set(pal[4:-4] for pal in [[c for c in s] for c in range(ord('a'), ord('z') + 1) if c in s])
