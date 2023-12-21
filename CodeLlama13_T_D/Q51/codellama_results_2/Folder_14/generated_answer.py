
def if_contains_anagrams(str_list):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagram_count = 0
    for str1 in str_list:
        for str2 in str_list:
            if len(str1) >= 3 and len(str2) >= 3 and (str1.lower() != str2.lower()) and all([c in english_letters for c in (str1 + str2)]):
                anagram_count += 1
    return anagram_count <= 474
