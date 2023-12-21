
def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 66:
                    return False
    return True
