
def if_contains_anagrams(my_list):
    pairs = 0
    for i in range(len(my_list)):
        s1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            s2 = my_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    pairs += 1
                    if pairs > 52:
                        return False
    return True
