
def if_contains_anagrams(my_list):
    anagrams = set()
    for word in my_list:
        if len(word) >= 3:
            anagram = ''.join(sorted(word.lower()))
            if anagram not in anagrams:
                anagrams.add(anagram)
    return len(anagrams) >= 28
