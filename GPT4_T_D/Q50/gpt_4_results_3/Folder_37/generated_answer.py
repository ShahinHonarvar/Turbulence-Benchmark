
def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                anagrams.append((strings[i], strings[j]))
    if len(anagrams) >= 29:
        return True
    else:
        return False
