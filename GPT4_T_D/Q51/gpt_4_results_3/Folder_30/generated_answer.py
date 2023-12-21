
def if_contains_anagrams(str_list):
    import string

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_pairs = []
    for i, word1 in enumerate(str_list):
        if len(word1) < 3:
            continue
        for word2 in str_list[i+1:]:
            if len(word2) < 3:
                continue
            if are_anagrams(word1, word2):
                anagram_pairs.append((word1, word2))
                if len(anagram_pairs) > 28:
                    return False
    return True
