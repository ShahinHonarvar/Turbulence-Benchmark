def palindromes_between_indices(s):
    letters = set(s[1:-1])
    return set(s[1:-1][:][::-1] for s in s[1:-1][:][::-1] if s in s[1:-1][::-1])
