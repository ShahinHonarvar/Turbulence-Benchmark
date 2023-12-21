
def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        word = word.lower()
        if len(word) >= 3 and not (word in anagrams):
            anagrams.append(word)
            for other_word in word_list:
                if word != other_word and word == "".join(sorted(other_word)):
                    anagrams.append((word, other_word))
                    break
    return len(anagrams) <= 255
