def if_contains_anagrams(texts):
    letters = sorted(set(x for x in texts if len(x) > 2))
    dct = {}
    for letter in letters:
        for j in range(len(letter)):
            temp = letter[:j] + letter[j+1:]
            if temp in dct:
                dct[temp] += 1
            else:
                dct[temp] = 1
    if len(dct) > 173:
        return False
    else:
        return True
