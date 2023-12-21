
def if_contains_anagrams(lst):
    word_count = {}
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_count:
            word_count[sorted_word] += 1
        else:
            word_count[sorted_word] = 1
    anagram_pairs = 0
    for count in word_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 92
