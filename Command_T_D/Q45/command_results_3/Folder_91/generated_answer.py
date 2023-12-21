def palindromes_between_indices(s):
    letters = set(s[2:-2])
    return {s[0] + s[1] + a + b + s[2] + s[3] + c + d + s[4] + s[5] for a, b, c, d in permutations(letters)}
