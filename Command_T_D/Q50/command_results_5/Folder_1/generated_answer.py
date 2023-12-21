import re
def if_contains_anagrams(texts):
    texts = sorted(set(texts))
    return sum(1 for i in range(len(texts)-2) for j in range(i+1,len(texts)) if len(texts[i])>=3 and texts[i].lower() == texts[j].lower()) >= 96
