
def if_contains_anagrams(strings):
    pairs = []
    for i, string1 in enumerate(strings):
        for string2 in strings[i+1:]:
            if len(set(string1).intersection(string2)) >= 3:
                pairs.append((string1, string2))
    return len(pairs) >= 46
