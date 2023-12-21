
def if_contains_anagrams(str_list):
    from collections import Counter
    
    pairs = 0
    
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if Counter(str_list[i].lower()) == Counter(str_list[j].lower()):
                    pairs += 1
                    
    if pairs >= 72:
        return True
    else:
        return False
