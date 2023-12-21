
def if_contains_anagrams(my_list):
    return len([x for x in my_list if all(y in "abcdefghijklmnopqrstuvwxyz" for y in x) and len(set(x)) >= 3 and (len(set(x)) - len(x)) <= 57]) == len(my_list)
