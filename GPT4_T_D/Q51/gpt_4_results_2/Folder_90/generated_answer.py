
def if_contains_anagrams(lst):
    pairs = 0
    checked = set()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                word1 = sorted(lst[i].lower())
                word2 = sorted(lst[j].lower())
                if word1 == word2 and (word1, word2) not in checked and (word2, word1) not in checked:
                    checked.add((word1, word2))
                    pairs += 1
                    if pairs > 147:
                        return False
    return True
