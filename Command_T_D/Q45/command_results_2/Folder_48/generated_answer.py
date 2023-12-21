def palindromes_between_indices(s):
    s = set(s)
    return {s[:4] + s[-4:] for s in s}
