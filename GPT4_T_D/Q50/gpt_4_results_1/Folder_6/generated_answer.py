
def if_contains_anagrams(str_list):
    anagram_dict = {}
    for word in str_list:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    pairs = sum([i//2 for i in anagram_dict.values()])
    return pairs >= 26
