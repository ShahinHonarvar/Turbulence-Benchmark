
def if_contains_anagrams(my_list):
    return len([i for i in my_list if len(set(i)) >= 3 and len(set(''.join(j[::-1] for j in i))) <= 14]) > 0
