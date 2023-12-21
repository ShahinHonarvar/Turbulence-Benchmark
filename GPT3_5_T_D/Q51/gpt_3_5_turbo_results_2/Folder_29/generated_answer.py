
def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                pairs += 1
                if pairs > 318:
                    return False
    return True
