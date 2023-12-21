def palindromes_between_indices(s):
    letters = set(s[2:-2])
    return set("".join(sorted(str(e))) for e in letters if str(e)[::-1] == str(e))
