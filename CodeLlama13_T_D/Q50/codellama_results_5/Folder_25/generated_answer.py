
def if_contains_anagrams(str_list):
    return len([i for i in str_list if len(i) >= 3 and set(i.lower()) in (j.lower() for j in str_list[str_list.index(i)+1:] if len(j) >= 3 else [])]) >= 14
