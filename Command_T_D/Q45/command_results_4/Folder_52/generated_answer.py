def palindromes_between_indices(s):
    return {p for i in range(len(s)) for p in palindromes(s[i:i+8])}
def palindromes(s):
    return {p for p in set(''.join(a).lower() for a in permutations(s)) if p == p[::-1]}
