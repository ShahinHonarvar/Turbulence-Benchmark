
from collections import defaultdict

def if_contains_anagrams(lst):
    def count_anagrams(lst):
        d = defaultdict(int)
        for word in lst:
            key = "".join(sorted(word.lower()))
            if len(key) >= 3:
                d[key] += 1
        return sum(v*(v-1)//2 for v in d.values())
    return count_anagrams(lst) <= 147
