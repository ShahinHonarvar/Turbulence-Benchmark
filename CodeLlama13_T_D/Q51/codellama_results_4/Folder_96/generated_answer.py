
def if_contains_anagrams(string_list):
    pairs = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            s1 = string_list[i].lower()
            s2 = string_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    pairs += 1
                    if pairs > 2:
                        return False
    return True
