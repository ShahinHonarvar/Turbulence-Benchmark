
from collections import Counter
def if_contains_anagrams(lst):
    hold = []
    for word in lst:
        word = ''.join(sorted(word.lower()))
        hold.append(word)
    count = Counter(hold)
    match = 0
    for key in count:
        if len(key) > 2:
            match += count[key]//2
            if match >= 98:
                return True
    return False
