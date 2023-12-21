
def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    for word in list_of_strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += 1
        if count > 2:
            return False
    return True
