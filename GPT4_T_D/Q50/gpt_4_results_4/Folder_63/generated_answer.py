
def if_contains_anagrams(words):
    from collections import defaultdict
    sorted_word_dict = defaultdict(list)
    anagram_count = 0
    words = [word.lower() for word in words if len(word) >= 3]
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_word_dict[sorted_word].append(word)
    for word_list in sorted_word_dict.values():
        length = len(word_list)
        if length > 1:
            anagram_count += length*(length-1) // 2
        if anagram_count >= 89:
            return True
    return False
