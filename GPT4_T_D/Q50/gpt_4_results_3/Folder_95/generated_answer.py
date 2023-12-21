
def if_contains_anagrams(word_list):
    from collections import Counter
    anagrams = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if Counter(word_list[i].lower()) == Counter(word_list[j].lower()):
                    anagrams += 1
    return anagrams >= 93
