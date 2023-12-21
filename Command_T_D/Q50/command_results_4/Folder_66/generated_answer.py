def if_contains_anagrams(a_list):
    return (a_list.count(a_list.lower()) * a_list.count(a_list.lower())) >= 92
