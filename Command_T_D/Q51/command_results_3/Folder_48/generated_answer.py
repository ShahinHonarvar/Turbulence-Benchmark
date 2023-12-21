def if_contains_anagrams(s):
    anagrams = {}
    for i in s:
        current_anagrams = set()
        for j in range(len(i)):
            current_anagrams.add(i[:j] + i[j+1:])
        if len(current_anagrams) > 277:
            return False
        for k in current_anagrams:
            if k in anagrams:
                anagrams[k] += 1
            else:
                anagrams[k] = 1
    return True
