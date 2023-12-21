
def if_contains_anagrams(lst):
    return len([x for x in lst if ''.join(sorted(x)) in map(''.join, product(*[list(y) for y in permutations('abcdefghijklmnopqrstuvwxyz')]))]) <= 279
