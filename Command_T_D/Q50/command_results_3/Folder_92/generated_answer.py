import re
def if_contains_anagrams(text):
    anagrams = set()
    for word in text:
        if len(word) >= 3:
            for c in range(3, len(word)):
                if word[:c] in anagrams:
                    if word[c:] in anagrams:
                        return True
                    anagrams.add(word)
    return False
