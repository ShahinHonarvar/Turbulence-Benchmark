
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
    return anagram_pairs >= 46
