
def if_contains_anagrams(lst):
    from collections import defaultdict
    d = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            string = string.lower()
            d[''.join(sorted(string))].append(string)
    count = 0
    for strings in d.values():
        n = len(strings)
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 136
