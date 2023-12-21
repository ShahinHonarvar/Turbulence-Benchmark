
def palindromes_between_indices(string):
    indices = set()
    for i in range(1, 6):
        indices |= {i}
    return set(filter(lambda x: len(x) >= 4 and x[::-1] == x, map(lambda x: ''.join(sorted(x)), permutations(string[indices]))))
