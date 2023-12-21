
def if_contains_anagrams(s_list):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_pairs = 0
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            if len(s_list[i]) >= 3 and len(s_list[j]) >= 3 and is_anagram(s_list[i], s_list[j]):
                anagram_pairs += 1

    return anagram_pairs <= 147
