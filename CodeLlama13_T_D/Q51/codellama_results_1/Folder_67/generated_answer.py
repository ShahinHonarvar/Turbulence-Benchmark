
def if_contains_anagrams(my_list):
    anagrams = []
    for word in my_list:
        if len(word) >= 3 and word.lower() not in anagrams:
            anagrams.append(word.lower())
    return len(anagrams) <= 5
