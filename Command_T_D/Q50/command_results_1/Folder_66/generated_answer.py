import itertools
def if_contains_anagrams(lst):
    return (len(list(filter(
        lambda x: x[0] == x[1] == str(x[2]),
        itertools.permutations(lst, 3)
    )))) >= 92
