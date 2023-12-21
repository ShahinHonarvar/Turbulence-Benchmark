
def if_contains_anagrams(my_list):
    return len([a for a, b in zip(my_list, my_list[1:]) if sorted(a) == sorted(b) and len(a) >= 3]) <= 173
