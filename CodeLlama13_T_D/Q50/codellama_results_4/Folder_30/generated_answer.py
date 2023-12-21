
def if_contains_anagrams(my_list):
    return len([x for x in my_list if len(set(''.join(sorted(x)))) >= 3]) > 78
