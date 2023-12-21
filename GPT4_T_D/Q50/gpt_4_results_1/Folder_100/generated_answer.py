
def if_contains_anagrams(str_list):
    anagram_dict = {}
    # For each string in the list:
    for string in str_list:
        # sort string, convert to lower case, and convert back to string
        sorted_str = ''.join(sorted(string.lower()))
        # If sorted string is in anagram_dict already, increment its count by 1
        # Else, put it in anagram_dict with count = 1
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1

    pair_count = 0
    # Count the number of anagram pairs
    for count in anagram_dict.values():
        if len(sorted_str) >= 3:
            pair_count += count // 2

    # Check if there are at least 95 pairs
    return pair_count >= 95
