
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            word1 = "".join(sorted(lst[i].lower()))
            word2 = "".join(sorted(lst[j].lower()))
            if (word1 == word2 and len(word1)>=3 and len(word2)>=3):
                pairs += 1
                if pairs >= 88:
                    return True
    return False
