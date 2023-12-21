
def if_contains_anagrams(strs):
    anagrams = []
    for i in range(len(strs)):
        for j in range(i+1, len(strs)):
            if strs[i].lower() == strs[j].lower():
                continue
            if len(strs[i]) < 3:
                break
            if len(anagrams) >= 4:
                return True
            anagrams.append((strs[i], strs[j]))
    return False
