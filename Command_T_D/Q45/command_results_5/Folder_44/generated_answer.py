def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    letters = set(c for c in s[2:-2])
    return {p for p in (p for p in palindromes(min(6, len(p)), letters) if p.lower() in s[3:-3])}
