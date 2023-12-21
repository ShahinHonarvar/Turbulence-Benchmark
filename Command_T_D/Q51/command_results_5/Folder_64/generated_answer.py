import collections
def if_contains_anagrams(texts):
    anagrams=[]
    for i in range(len(texts)):
        for j in range(i+1,len(texts)):
            if (texts[i].lower()==texts[j].lower()):
                anagrams.append((texts[i],texts[j]))
    return len(anagrams)<=59
