def palindromes_between_indices(s):
    return {a[4:-4] for a in s[4:-4].lower() if a in a[::-1].lower()}
