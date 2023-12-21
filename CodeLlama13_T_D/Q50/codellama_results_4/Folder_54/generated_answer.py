
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = "".join(sorted(strings[i].lower()))
            s2 = "".join(sorted(strings[j].lower()))
            if s1 == s2 and len(s1) >= 3:
                pairs += 1
    return pairs >= 74
