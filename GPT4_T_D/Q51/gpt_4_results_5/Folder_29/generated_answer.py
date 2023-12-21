
def if_contains_anagrams(lst):
    import collections
    def count_anagram_pairs(lst):
        counts = collections.defaultdict(int)
        for word in lst:
            counts[str(sorted(word.lower()))] += 1
        return sum(v*(v-1)//2 for v in counts.values() if v >= 2 and len(list(counts.keys())[0]) >= 3)
    return count_anagram_pairs(lst) <= 318
