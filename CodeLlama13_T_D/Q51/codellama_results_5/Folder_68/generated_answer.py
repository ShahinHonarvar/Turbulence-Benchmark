
def if_contains_anagrams(my_list):
    return len([i for i in my_list if len(set(j for j in i)) > 3]) <= 94
