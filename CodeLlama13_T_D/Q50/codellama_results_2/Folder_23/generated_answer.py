
def if_contains_anagrams(string_list):
    return len([i for i in string_list if ''.join(sorted(i)) in string_list[1:] and not i.lower() == ''.join(sorted(i)).lower()]) >= 67
