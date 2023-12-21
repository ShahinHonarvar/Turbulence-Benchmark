import collections
def if_contains_anagrams(texts):
    anagrams=[]
    for s in sorted(texts):
        if s in anagrams:
            continue
        for i in range(len(s)-2):
            temp=s[:i]+s[i+1:]
            if temp in anagrams:
                break
            anagrams.append(s)
            if len(anagrams)>60:
                return False
    return True
