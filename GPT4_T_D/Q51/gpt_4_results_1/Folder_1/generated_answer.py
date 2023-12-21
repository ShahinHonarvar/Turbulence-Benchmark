
from collections import Counter

def isAnagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(strList):
    pairs = 0
    for i in range(len(strList)):
        for j in range(i+1, len(strList)):
            str1 = strList[i].lower()
            str2 = strList[j].lower()            
            if len(str1) >= 3 and len(str2) >= 3 and isAnagram(str1, str2):
                pairs += 1
                if pairs > 30:
                    return False
    return True
