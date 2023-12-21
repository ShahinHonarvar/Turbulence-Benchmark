
def if_contains_anagrams(str_list):
    anagram_pairs = []
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            str1, str2 = str_list[i].lower(), str_list[j].lower()
            if sorted(str1) == sorted(str2):
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) <= 5
