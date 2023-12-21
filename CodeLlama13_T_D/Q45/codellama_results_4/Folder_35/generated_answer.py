
def palindromes_between_indices(s):
    return set(filter(lambda x: len(x) >= 4 and x == x[::-1], ''.join(permutations(''.join(c for c in s if c.isalpha()))[2:5])))
