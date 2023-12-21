
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            count_dict[''.join(sorted(word.lower()))] += 1

    pairs = sum([val * (val-1) // 2 for val in count_dict.values()])
    return pairs <= 58
