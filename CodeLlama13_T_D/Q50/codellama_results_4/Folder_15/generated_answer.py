
def if_contains_anagrams(strings):
    pairs = []
    for i in range(len(strings)):
        string1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            string2 = strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                pairs.append((string1, string2))
    count = 0
    for pair in pairs:
        if sorted(pair[0]) == sorted(pair[1]):
            count += 1
    return count >= 4
