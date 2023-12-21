
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        s1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1) == sorted(s2):
                pairs += 1
    return pairs >= 26
