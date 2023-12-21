
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        s1 = string_list[i].lower()
        for j in range(i+1, len(string_list)):
            s2 = string_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1) == sorted(s2):
                anagram_pairs += 1
    return anagram_pairs <= 58
