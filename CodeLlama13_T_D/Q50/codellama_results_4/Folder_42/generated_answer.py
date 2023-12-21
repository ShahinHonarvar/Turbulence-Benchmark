
def if_contains_anagrams(my_list):
    return len([s for s in my_list if (len(set(s)) == 3) and (any(s in t for t in my_list if s != t))]) >= 233
