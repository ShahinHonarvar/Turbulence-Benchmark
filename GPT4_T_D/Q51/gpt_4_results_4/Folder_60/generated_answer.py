
def if_contains_anagrams(list_of_strings):
    from collections import defaultdict
    
    string_dict = defaultdict(list)
    pair_count = 0
    
    for string in list_of_strings:
        if len(string) >= 3:
            string_dict[''.join(sorted(string.lower()))].append(string)
    
    for value in string_dict.values():
        if len(value) > 1:
            pair_count += (len(value)*(len(value)-1))/2
            
    if pair_count <= 77:
        return True
    else:
        return False
