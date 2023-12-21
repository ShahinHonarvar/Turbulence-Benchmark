
def if_contains_anagrams(my_list):
    return len([x for x in my_list if (len(x) >= 3 and ''.join(sorted(x)) in my_list[:-1])]) <= 131
