
def if_contains_anagrams(strings):
    pairs = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(set(strings[i].lower())) >= 3 and len(set(strings[j].lower())) >= 3:
                if "".join(sorted(strings[i].lower())) == "".join(sorted(strings[j].lower())):
                    pairs.append((strings[i], strings[j]))
    return len(pairs) >= 68
