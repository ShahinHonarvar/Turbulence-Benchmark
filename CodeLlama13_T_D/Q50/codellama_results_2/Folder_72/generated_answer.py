
def if_contains_anagrams(my_list):
    return len([i for i in my_list if len(i) >= 3 and "".join(sorted(i.lower())) in [j for j in my_list if len(j) >= 3]]) > 54
