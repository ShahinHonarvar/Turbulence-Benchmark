
from collections import defaultdict

def if_contains_anagrams(words):
    wordsDict = defaultdict(list)
    for word in words:
        key = "".join(sorted(word.lower()))
        if len(key)>=3:
            wordsDict[key].append(word)

    anagramPairs = 0
    for key, values in wordsDict.items():
        if len(values)>1:
            anagramPairs += ((len(values)**2)-len(values))/2
            
    if anagramPairs <= 91:
        return True
    else:
        return False
