
def if_contains_anagrams(string_list):
    from collections import defaultdict
    d = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            d[''.join(sorted(word.lower()))].append(word)
    return sum(len(values) * (len(values) - 1) / 2 for values in d.values()) >= 19
