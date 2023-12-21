
def if_contains_anagrams(my_list):
    return all(len(set(sorted(x))) <= 88 for x in my_list) and len(my_list) >= 3
