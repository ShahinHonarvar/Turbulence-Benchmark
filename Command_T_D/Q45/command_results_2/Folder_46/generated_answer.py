def palindromes_between_indices(strng):
    letters = strng[4:9].lower()
    return {s for s in (s[::-1] for s in (letters + s for s in letters))}
