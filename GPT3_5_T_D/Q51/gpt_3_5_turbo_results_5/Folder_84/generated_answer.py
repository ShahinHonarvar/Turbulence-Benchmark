
def if_contains_anagrams(lst):
    pairs = 0
    anagrams = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    if lst[i].lower() not in anagrams and lst[j].lower() not in anagrams:
                        pairs += 1
                        anagrams.append(lst[i].lower())
                        anagrams.append(lst[j].lower())
                        break
    return pairs <= 16
