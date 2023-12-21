def palindromes_between_indices(s):
    return {p for p in ("".join(l[7:-1]) for l in ((s[i:j+1] for i in range(len(s)-7, -1, 1)))} if p.lower() == p and len(p) >= 3}
