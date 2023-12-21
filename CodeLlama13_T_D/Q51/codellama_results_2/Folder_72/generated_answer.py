
def if_contains_anagrams(my_list):
    return len([pair for pair in itertools.combinations(my_list, 2) if sorted(pair[0].lower()) == sorted(pair[1].lower())]) <= 188
