
def if_contains_anagrams(my_list):
    anagrams = set()
    for word in my_list:
        word_lower = word.lower()
        if len(word_lower) >= 3 and word_lower not in anagrams:
            anagrams.add(word_lower)
            for i in range(len(anagrams)):
                if anagrams[i] == "".join(sorted(word_lower)) and len(anagrams) <= 84:
                    return True
        else:
            continue
    return False
