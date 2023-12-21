
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for string1 in string_list:
        for string2 in string_list[1:]:
            if is_anagram(string1, string2) and len(string1) >= 3:
                anagram_pairs += 1
    return anagram_pairs <= 44
