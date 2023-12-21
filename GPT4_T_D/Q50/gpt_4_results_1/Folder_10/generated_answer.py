
def if_contains_anagrams(strings_list):
    anagram_dict = dict()
    for word in strings_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = 0
    for word_list in anagram_dict.values():
        word_count = len(word_list)
        if word_count > 1:
            anagram_pairs += word_count * (word_count - 1) // 2
    return anagram_pairs >= 52
