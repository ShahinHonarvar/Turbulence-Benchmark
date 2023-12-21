def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    max_l = max(13, len(s) - 17)
    return {w for w in set(w for w in s[17:-95] if len(w) <= max_l) if w in w[::-1].lower() and all(c.isalpha() for c in w)}
