
def if_contains_anagrams(str_list):
    for str1 in str_list:
        for str2 in str_list:
            if len(str1) >= 3 and len(str2) >= 3 and len(set(str1.lower())) == len(set(str2.lower())) and set(str1.lower()) != set(str2.lower()):
                return True
    return False
