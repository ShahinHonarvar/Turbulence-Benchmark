
def if_contains_anagrams(str_list):
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(set(str_list[i].lower())) >= 3 and len(set(str_list[j].lower())) >= 3:
                if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                    pairs += 1
                    break
    return pairs >= 20
