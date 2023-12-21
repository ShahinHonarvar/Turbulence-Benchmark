
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    pairs += 1
                    if pairs >= 314:
                        return True
    return False
