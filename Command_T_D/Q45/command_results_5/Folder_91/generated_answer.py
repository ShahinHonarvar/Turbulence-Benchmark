def palindromes_between_indices(s):
    letters = sorted(set(s[2:-6:-1]))
    return set(
        (s[0] + s[1] + l + s[-1] + s[-2] for l in letters)
        if len(s) > 2 and len(letters) >= 3
    )
