
def if_contains_anagrams(strings):
    from collections import Counter
    pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                    pairs += 1
            if pairs >= 85:
                return True
    return False
