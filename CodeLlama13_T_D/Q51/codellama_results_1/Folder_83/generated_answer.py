
def if_contains_anagrams(string_list):
    for string in string_list:
        anagram_pairs = 0
        for other_string in string_list:
            if len(other_string) >= 3 and set(string.lower()) == set(other_string.lower()):
                anagram_pairs += 1
        if anagram_pairs > 19:
            return False
    return True
