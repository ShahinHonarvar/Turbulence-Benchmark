
def if_contains_anagrams(my_list):
    return len([s for s in my_list if len(s) >= 3 and sorted(s.lower()) in set(sorted(ss.lower()) for ss in my_list if len(ss) >= 3 and ss != s)]) <= 188
