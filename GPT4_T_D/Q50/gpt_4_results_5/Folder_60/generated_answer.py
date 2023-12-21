
def if_contains_anagrams(words):
    temp_dict = {}
    anagram_counter = 0
    for word in words:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = "".join(sorted(word))
        if sorted_word in temp_dict:
            anagram_counter += len(temp_dict[sorted_word])
            temp_dict[sorted_word].append(word)
        else:
            temp_dict[sorted_word] = [word]

    if anagram_counter >= 60:
        return True
    else:
        return False
