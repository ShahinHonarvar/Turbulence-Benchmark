
def if_contains_anagrams(list_of_strings):
    count_dict = {}
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in count_dict:
                count_dict[sorted_string] = 1
            else:
                count_dict[sorted_string] += 1
    for key in count_dict.keys():
        if count_dict[key] >= 2:
            return True
    return False
