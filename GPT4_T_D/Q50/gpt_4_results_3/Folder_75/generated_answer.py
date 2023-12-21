
def if_contains_anagrams(lst):
    from collections import defaultdict

    def count_anagrams(lst):
        d = defaultdict(list)
        for word in lst:
            if len(word) >= 3:
                d["".join(sorted(word.lower()))].append(word)
        return sum(len(v)*(len(v)-1)//2 for v in d.values() if len(v)>1)

    return count_anagrams(lst) >= 70
