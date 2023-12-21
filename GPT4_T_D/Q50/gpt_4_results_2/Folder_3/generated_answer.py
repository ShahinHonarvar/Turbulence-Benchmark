
def if_contains_anagrams(lst):
    from collections import defaultdict

    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)

    count = sum(len(values)*(len(values)-1)//2 for values in word_dict.values() if len(values) > 1)

    return count >= 30
