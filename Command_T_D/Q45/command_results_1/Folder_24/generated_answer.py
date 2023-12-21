def palindromes_between_indices(s):
    return {w[::-1] for w in ("".join(c for c in s[2:-2]) for c in range(10)) if len(w) >= 4}
