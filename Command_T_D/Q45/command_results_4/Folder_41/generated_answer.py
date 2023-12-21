def palindromes_between_indices(s):
    return set((''.join(sorted(l)) for l in zip(*map(str.lower, (s[2:-2], s[2:-1], s[2:-3])))))
