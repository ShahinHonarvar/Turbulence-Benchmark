
def if_contains_anagrams(string_list):
    from collections import Counter
    valid_anagram_dict = {}
    count = 0

    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in valid_anagram_dict:
                valid_anagram_dict[sorted_string] = 1
            else:
                count += valid_anagram_dict[sorted_string]
                valid_anagram_dict[sorted_string] += 1

    return count >= 74
