
def if_contains_anagrams(my_list):
    return len([x for x in my_list if ''.join(sorted(x)) in my_list]) <= 289
