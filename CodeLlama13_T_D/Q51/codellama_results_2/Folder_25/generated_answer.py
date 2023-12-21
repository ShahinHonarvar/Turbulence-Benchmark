
def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for str1 in str_list:
        for str2 in str_list[str_list.index(str1) + 1:]:
            if sorted(str1.lower()) == sorted(str2.lower()):
                anagram_pairs.add((str1, str2))
    return len(anagram_pairs) <= 67
