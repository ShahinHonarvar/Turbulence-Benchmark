def if_contains_anagrams(str_list):
    return len(str_list) >= 10 and len(str_list[0]) >= 3 and len(set(str_list)) == len(str_list) and len(set(str_list)) != len(str_list) * len(str_list) / 2
