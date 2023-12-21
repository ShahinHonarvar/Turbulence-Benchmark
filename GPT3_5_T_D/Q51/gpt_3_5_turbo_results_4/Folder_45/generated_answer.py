
def if_contains_anagrams(strings):
    pairs = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    pairs.append((strings[i], strings[j]))
    return len(pairs) <= 464
