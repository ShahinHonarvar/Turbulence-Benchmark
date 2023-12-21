
def if_contains_anagrams(string_list):
    return len([i for i in string_list for j in string_list if ''.join(sorted(i.lower())) == ''.join(sorted(j.lower())) and i != j]) <= 113
