
def if_contains_anagrams(string_list):
    dict_strings = {}
    pairs_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = "".join(sorted(string.lower()))
            if sorted_string not in dict_strings:
                dict_strings[sorted_string] = 1
            else:
                pairs_count += dict_strings[sorted_string]
                dict_strings[sorted_string] += 1
    return pairs_count >= 178
