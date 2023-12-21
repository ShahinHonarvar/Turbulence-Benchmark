def palindromes_between_indices(s):
    if not s:
        return set()
    return set(s[0:4] + s[2:-2] + s[-2:-4] + s[-4:])
