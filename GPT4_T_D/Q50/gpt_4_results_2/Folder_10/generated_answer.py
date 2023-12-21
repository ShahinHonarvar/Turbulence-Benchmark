
def if_contains_anagrams(str_list):
    anagrams_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]
    anagrams_count = sum(len(words)-1 for words in anagrams_dict.values() if len(words) > 1)
    return anagrams_count >= 52
