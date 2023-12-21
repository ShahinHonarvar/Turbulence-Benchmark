
def if_contains_anagrams(str_list):
    from collections import Counter
    
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    pairs_found = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if is_anagram(str_list[i].lower(), str_list[j].lower()):
                    pairs_found += 1
                    if pairs_found > 464:
                        return False

    return True
