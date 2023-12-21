
def if_contains_anagrams(my_list):
    return len([p for p in itertools.combinations(my_list, 2) if "".join(sorted(p[0])) == "".join(sorted(p[1]))]) <= 89
