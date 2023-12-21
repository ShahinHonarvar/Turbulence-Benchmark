
def if_contains_anagrams(str_lst):
    from collections import defaultdict
    
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1) == sorted(str2)
    
    pairs_num = 0
    i = 0
    while i < len(str_lst)-1:
        for str2 in str_lst[i+1:]:
            if is_anagram(str_lst[i], str2):
                pairs_num += 1
                if pairs_num >= 276:
                    return True
        i += 1
    return False
