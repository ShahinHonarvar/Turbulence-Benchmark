
def if_contains_anagrams(string_list):
    anagram_pairs = []
    for i in range(len(string_list)):
        s1 = string_list[i].lower()
        for j in range(i+1, len(string_list)):
            s2 = string_list[j].lower()
            if sorted(s1) == sorted(s2):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) >= 20
