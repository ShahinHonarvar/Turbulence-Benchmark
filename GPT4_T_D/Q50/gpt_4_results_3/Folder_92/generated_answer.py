
def if_contains_anagrams(list_of_words):
    word_dict = {}

    for word in list_of_words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in word_dict:
            word_dict[sorted_word] += 1
        else:
            word_dict[sorted_word] = 1

    pairs_of_anagrams = sum(value // 2 for value in word_dict.values())

    if pairs_of_anagrams >= 2:
        return True
    else:
        return False
