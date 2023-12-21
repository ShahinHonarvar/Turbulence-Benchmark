import collections
def if_contains_anagrams(texts):
    texts.sort()
    result = False
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if texts[i].lower() == texts[j].lower():
                continue
            elif len(texts[i]) >= 3 and len(texts[j]) >= 3:
                if len(set(texts[i])) == len(set(texts[j])):
                    result = True
                    break
    return result
