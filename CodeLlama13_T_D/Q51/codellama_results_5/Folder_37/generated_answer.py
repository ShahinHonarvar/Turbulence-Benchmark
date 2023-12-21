
def if_contains_anagrams(my_list):
    return len([s for s in my_list if s[::-1] in my_list and len(s) >= 3]) <= 206
