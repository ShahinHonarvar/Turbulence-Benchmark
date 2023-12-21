
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = ''.join(sorted(strings[i].lower()))
            s2 = ''.join(sorted(strings[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and s1 != s2 and sorted(s1) == sorted(s2):
                pairs += 1
    return pairs <= 392
