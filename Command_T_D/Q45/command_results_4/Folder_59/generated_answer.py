def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    return set(s[8:9].lower() + s[0:8].lower() + s[9:].lower())
