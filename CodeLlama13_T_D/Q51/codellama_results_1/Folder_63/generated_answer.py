
def if_contains_anagrams(string_list):
    for s1 in string_list:
        for s2 in string_list:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                return True
    return False
