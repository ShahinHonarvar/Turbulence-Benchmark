
from collections import Counter

def if_contains_anagrams(lst):
    count = 0

    for i, s1 in enumerate(lst):
        counter1 = Counter(s1.lower())

        if len(s1) >= 3:
            for s2 in lst[i+1:]:
                counter2 = Counter(s2.lower())

                if counter1 == counter2:
                    count += 1

                    if count > 49:
                        return False
                    
    return True
