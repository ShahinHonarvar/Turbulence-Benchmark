
def if_contains_avagrams(lst):
    from collections import defaultdict
    pairs = 0
    dict_ = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        word = ''.join(sorted(word.lower()))
        dict_[word] += 1
    for key in dict_:
        pairs += dict_[key] * (dict_[key] - 1) // 2
    return pairs >= 72
