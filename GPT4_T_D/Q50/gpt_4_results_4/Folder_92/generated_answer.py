
def if_contains_anagrams(word_list):
    anagram_dict = {}
    for word in word_list:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    anagram_pairs = sum([count // 2 for count in anagram_dict.values()])
    return anagram_pairs >= 2
