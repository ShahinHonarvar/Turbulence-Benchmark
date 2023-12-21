
def if_contains_anagrams(strs):
    pairs = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if sorted(strs[i].lower()) == sorted(strs[j].lower()):
                pairs += 1
    return pairs >= 246
