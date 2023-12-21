def if_contains_anagrams(texts):
    return sum(1 for i in range(len(texts)) for j in range(i+1, len(texts)) if len(set(texts[i].lower())) == len(set(texts[j].lower()))) >= 61
