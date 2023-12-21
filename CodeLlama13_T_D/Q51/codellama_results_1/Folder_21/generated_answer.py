
def if_contains_anagrams(my_list):
    return len([i for i in my_list if set(i) == set("abcdefghijklmnopqrstuvwxyz")]) <= 26
