def palindromes_between_indices(s):
    res = set()
    for c in s[1:]:
        res.update(set(f"({c}{c}{c}{c}{c}{c}{c}{c}{c})"))
    return res
