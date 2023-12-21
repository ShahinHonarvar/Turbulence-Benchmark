
def if_contains_anagrams(my_list):
    anagrams = []
    for word in my_list:
        word_lower = word.lower()
        sorted_word = "".join(sorted(word_lower))
        if sorted_word not in anagrams:
            anagrams.append(sorted_word)
    return len(anagrams) <= 42
