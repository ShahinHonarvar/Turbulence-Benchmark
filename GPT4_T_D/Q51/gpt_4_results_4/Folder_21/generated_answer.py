
def if_contains_anagrams(lst):
    from collections import Counter

    lst = [word.lower() for word in lst if len(word) >= 3]

    anagram_pairs = []
    for word in lst:
        word_counter = Counter(word)
        for other_word in lst:
            if other_word != word and word_counter == Counter(other_word):
                if sorted([word, other_word]) not in anagram_pairs:
                    anagram_pairs.append(sorted([word, other_word]))

    return len(anagram_pairs) <= 26
