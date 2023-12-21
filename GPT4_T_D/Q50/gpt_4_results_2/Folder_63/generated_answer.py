
def if_contains_anagrams(str_list):
    anagram_dict = {}
    anagram_pair_count = 0

    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = "".join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    for word, anagrams in anagram_dict.items():
        anagram_count = len(anagrams)
        if anagram_count >= 2:
            anagram_pair_count += (anagram_count*(anagram_count-1))//2
        if anagram_pair_count >= 89:
            return True

    return False
