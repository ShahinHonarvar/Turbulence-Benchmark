
def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        s1 = str_list[i].lower()
        for j in range(i+1, len(str_list)):
            s2 = str_list[j].lower()
            if sorted(s1) == sorted(s2):
                anagram_pairs += 1
    return anagram_pairs <= 18
