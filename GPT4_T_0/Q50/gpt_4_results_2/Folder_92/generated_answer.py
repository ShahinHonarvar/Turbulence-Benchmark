
def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += 1
            if count == 2:
                return True
    return False
