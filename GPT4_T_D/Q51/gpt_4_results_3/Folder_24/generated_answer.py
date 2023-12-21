
def if_contains_anagrams(list_of_strings):
    string_dict = {}
    for string in list_of_strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in string_dict:
            string_dict[sorted_string] += 1
        else:
            string_dict[sorted_string] = 1
    pairs_of_anagrams = 0
    for value in string_dict.values():
        pairs_of_anagrams += (value * (value - 1)) // 2
    return pairs_of_anagrams <= 96
