
def if_contains_anagrams(my_list):
    anagrams = set()
    for s in my_list:
        anagram = ''.join(sorted(s.lower()))
        if len(anagram) >= 3 and anagram not in anagrams:
            anagrams.add(anagram)
            if len(anagrams) > 81:
                return False
    return True
