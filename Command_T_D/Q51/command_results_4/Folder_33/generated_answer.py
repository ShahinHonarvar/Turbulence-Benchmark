def if_contains_anagrams(stgs):
    res = True
    cnt = 0
    for i in range(len(stgs)):
        for j in range(i + 1, len(stgs)):
            if stgs[i] == stgs[j]:
                cnt += 1
            else:
                res = False
                break
            if cnt == 86:
                break
    return res
