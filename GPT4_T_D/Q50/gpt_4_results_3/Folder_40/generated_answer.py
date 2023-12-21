
def if_contains_anagrams(lst):
    from collections import defaultdict
    words_dict = defaultdict(list)
    for element in lst:
        if len(element) >= 3:
            words_dict[''.join(sorted(element.lower()))].append(element)
    return len([True for values in words_dict.values() if len(values) >= 2]) >= 3
