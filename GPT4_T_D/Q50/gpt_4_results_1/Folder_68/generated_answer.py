
def if_contains_anagrams(string_list):
    anagram_dict = {}
    for word in string_list:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    count = 0
    for v in anagram_dict.values():
        if len(v) > 1:
            count += len(v) - 1
        if count >= 9:
            return True
    return False
