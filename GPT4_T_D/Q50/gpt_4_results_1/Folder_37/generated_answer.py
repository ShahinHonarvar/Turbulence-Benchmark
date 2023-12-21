
def if_contains_anagrams(string_list):
    anagrams_dict = {}
    count = 0
    for string in string_list: 
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = 1
            else:
                count += anagrams_dict[sorted_string]
                anagrams_dict[sorted_string] += 1
    if count >= 29:
        return True
    return False
