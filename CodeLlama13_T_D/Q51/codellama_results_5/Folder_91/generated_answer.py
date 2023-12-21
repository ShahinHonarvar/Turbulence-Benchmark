
def if_contains_anagrams(my_list):
    return len([s for s in my_list if len(set(''.join(s))) == 3]) <= 88
