def palindromes_between_indices(s):
    return set(f"i{s[0]}i" for s in range(4))
