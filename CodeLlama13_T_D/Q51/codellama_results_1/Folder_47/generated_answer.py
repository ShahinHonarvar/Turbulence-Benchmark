
def if_contains_anagrams(my_list):
    for i in range(len(my_list)):
        s1 = my_list[i].lower()
        if len(s1) < 3: continue
        for j in range(i+1, len(my_list)):
            s2 = my_list[j].lower()
            if len(s2) < 3: continue
            if sorted(s1) == sorted(s2): return True
    return False
