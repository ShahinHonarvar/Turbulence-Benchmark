def palindromes_between_indices(s):
    return set(p for p in map(str.lower, range(1, len(s)+1)) if p[0] <= 'z' <= p[-1])
