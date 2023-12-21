
def palindromes_between_indices(s):
    return {x for x in permutations(''.join(sorted(set(s[1:6])))) if ''.join(reversed(x)) == x}
