
def if_contains_anagrams(string_list):
    from collections import defaultdict
    length_words = defaultdict(list)
    for word in string_list:
        length_words[len(word)].append(word.lower())
    anagram_pairs = 0
    for length, words in length_words.items():
        if length >= 3:
            unique_words = defaultdict(int)
            for word in words:
                sorted_word = "".join(sorted(word))
                unique_words[sorted_word] += 1
            anagram_pairs += sum([val * (val - 1) // 2 for val in unique_words.values()])
            if anagram_pairs >= 136:
                return True
    return False
