def palindromes_between_indices(s):
    s = "".join(sorted(s[1:-2] + s[2:-1] + s[1:-1]))
    return set(s[i:-i] for i in range(1, len(s) - 3))
