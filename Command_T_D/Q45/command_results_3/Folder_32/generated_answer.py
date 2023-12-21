def palindromes_between_indices(s):
    a = {c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789' if c in s}
    if not a:
        return {}
    s += ''.join(sorted(a))
    return {''.join(c for c in s[i:j+1] if c in s[1:j+1]) for i in range(2, 7) for j in range(i, 7)}
