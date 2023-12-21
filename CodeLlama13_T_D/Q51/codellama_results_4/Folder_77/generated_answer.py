
def if_contains_anagrams(my_list):
    return len([s for s in my_list if len(s) >= 3 and ''.join(sorted(s)) in set(''.join(sorted(s)))]) <= 17
