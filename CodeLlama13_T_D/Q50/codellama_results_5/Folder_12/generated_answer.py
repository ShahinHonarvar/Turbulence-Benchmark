
def if_contains_anagrams(my_list):
    return len([x for x in my_list if x[::-1] in my_list]) >= 69
