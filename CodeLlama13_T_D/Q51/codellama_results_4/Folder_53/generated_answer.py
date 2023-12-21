
def if_contains_anagrams(my_list):
    return len([i for i in my_list if "".join(sorted(i)) in my_list[1:]]) <= 8
