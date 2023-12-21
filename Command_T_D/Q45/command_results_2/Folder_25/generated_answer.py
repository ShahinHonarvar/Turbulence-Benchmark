def palindromes_between_indices(s):
    d = {c: i for i, c in enumerate(s)}
    return set(f'{d[a][1]:s}{a}{d[b][1]:s}{b}' for a, b in zip(s[1:-1], s[2:-1]) if f'{d[a][1]:s}{a}{d[b][1]:s}{b}' in set(f'{d[a]:s}{b}' for b in s[1:-1])))
