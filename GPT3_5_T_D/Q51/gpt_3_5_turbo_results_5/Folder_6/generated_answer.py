
import collections

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        str1 = strings[i].lower()
        if len(str1) >= 3:
            for j in range(i+1, len(strings)):
                str2 = strings[j].lower()
                if len(str2) >= 3:
                    if collections.Counter(str1) == collections.Counter(str2):
                        count += 1
                        
    return count <= 86
