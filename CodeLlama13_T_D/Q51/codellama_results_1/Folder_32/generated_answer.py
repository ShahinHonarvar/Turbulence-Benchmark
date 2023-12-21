
def if_contains_anagrams(my_list):
    return len([s for s in my_list if len(set(s)) >= 3 and set(''.join(sorted(s))) in [set(''.join(sorted(x))) for x in my_list]]) <= 89
