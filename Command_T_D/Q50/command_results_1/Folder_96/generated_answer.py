import itertools
def if_contains_anagrams(text):
    return sum(1 for t in itertools.permutations(text) if t[0].lower() == t[1].lower()) >= 98
