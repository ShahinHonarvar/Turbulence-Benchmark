
def if_contains_anagrams(strings):
    return len([s for s in strings if s and len(s) >= 3 and ''.join(sorted(s)) in map(''.join, zip(*[itertools.combinations(strings, 2)]*len(strings)))]) >= 17
