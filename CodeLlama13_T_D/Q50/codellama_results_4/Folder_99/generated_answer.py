
def if_contains_anagrams(list):
    pairs = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i].lower() == list[j].lower():
                pairs += 1
    return pairs >= 314
