
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for string1 in string_list:
        for string2 in string_list[string_list.index(string1)+1:]:
            if len(set(string1).intersection(string2)) == len(set(string1)):
                anagram_pairs += 1
    return anagram_pairs <= 445
