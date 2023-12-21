
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for i in lst:
        if len(i) >= 3:
            sorted_i = "".join(sorted(i.lower()))
            anagram_dict[sorted_i].append(i)
    count = 0
    for _, value in anagram_dict.items():
        n = len(value)
        if n > 1:
            count += (n*(n-1))//2
        if count >= 49:
            return True
    return False
