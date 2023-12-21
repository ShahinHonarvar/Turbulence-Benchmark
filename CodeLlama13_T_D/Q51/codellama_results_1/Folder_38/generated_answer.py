
def if_contains_anagrams(my_list):
    return len([i for i in my_list if ''.join(sorted(i)) in set(''.join(sorted(j)) for j in my_list)]) <= 416
