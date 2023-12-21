
def if_contains_anagrams(mylist):
    anagrams = []
    for s in mylist:
        if len(s) >= 3 and s.lower() not in anagrams:
            anagrams.append(s.lower())
    return len(anagrams) <= 60
