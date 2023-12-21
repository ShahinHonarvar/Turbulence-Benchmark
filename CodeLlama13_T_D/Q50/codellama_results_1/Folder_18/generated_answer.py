
def if_contains_anagrams(str_list):
    count = 0
    for i in range(len(str_list)):
        s1 = str_list[i].lower()
        for j in range(i+1, len(str_list)):
            s2 = str_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    count += 1
                    if count >= 106:
                        return True
    return False
