
def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagrams.append((strings[i], strings[j]))
    return len(anagrams) <= 46 and all(len(a) >= 3 for a in anagrams)
