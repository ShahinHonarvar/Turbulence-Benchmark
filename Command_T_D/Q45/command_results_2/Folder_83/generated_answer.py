def palindromes_between_indices(s):
    return {x for x in map(str.lower, range(len(s) - 1, -1, -1)) if x[0] == x[x.index(x[0])] == x[x.rindex(x[0])] == x[len(x) // 2] == x[len(x) - 1] == x[0] and len(x) >= 7}
