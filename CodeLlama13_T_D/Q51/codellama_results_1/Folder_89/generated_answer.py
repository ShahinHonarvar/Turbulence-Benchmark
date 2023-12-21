
def if_contains_anagrams(my_list):
    anagram_pairs = []
    for word in my_list:
        word_lower = word.lower()
        if len(word_lower) >= 3 and word_lower not in anagram_pairs:
            anagram_pairs.append(word_lower)
            for other_word in my_list[my_list.index(word):]:
                other_word_lower = other_word.lower()
                if len(other_word_lower) >= 3 and word_lower != other_word_lower:
                    anagram_pairs.append((word_lower, other_word_lower))
    return len(anagram_pairs) <= 73
