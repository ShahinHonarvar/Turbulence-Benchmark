
def if_contains_anagrams(str_list):
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                    pairs += 1
                    if pairs >= 20:
                        return True
    return False
