
def if_contains_anagrams(list_of_strings):
    pairs = []
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            s1 = list_of_strings[i].lower()
            s2 = list_of_strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                pairs.append((s1, s2))
    return len(pairs) <= 173
