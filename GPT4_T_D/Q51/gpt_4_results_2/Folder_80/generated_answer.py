
def if_contains_anagrams(words_list):
    anagrams = {}
    for word in words_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    pairs_count = sum([len(words)*(len(words)-1)//2 for words in anagrams.values() if len(words) > 1])
    return pairs_count <= 255
