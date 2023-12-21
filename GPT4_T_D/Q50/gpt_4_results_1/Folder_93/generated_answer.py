
def if_contains_anagrams(str_list):
    counter = 0
    str_dict = {}
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if len(key)>=3 and key in str_dict:
            counter += str_dict[key]
            if counter >= 18:
                return True
        str_dict[key] = str_dict.get(key, 0) + 1
    return False
