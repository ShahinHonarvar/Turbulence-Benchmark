
def if_contains_anagrams(my_list):
    return len([p for p in zip(my_list, my_list[1:]) if p[0].lower() == p[1].lower()]) >= 97
