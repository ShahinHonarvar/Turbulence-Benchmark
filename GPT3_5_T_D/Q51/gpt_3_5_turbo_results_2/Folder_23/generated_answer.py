
def if_contains_anagrams(strings):
    from collections import Counter
    count = Counter()
    for string in strings:
        if len(string) < 3:
            continue
        count[tuple(sorted(string.lower()))] += 1
    return sum(v * (v - 1) // 2 for v in count.values()) <= 49
