
def if_contains_anagrams(str_list):
    anagram_count = 0
    for str1 in str_list:
        for str2 in str_list:
            if len(set(str1).intersection(str2)) >= 3 and set(str1.lower()) == set(str2.lower()):
                anagram_count += 1
    return anagram_count <= 77
