
def if_contains_anagrams(lst):
    from collections import Counter
    counter_list = [Counter(word.lower()) for word in lst if len(word) >= 3]
    pairs = [count for count in counter_list if counter_list.count(count) >= 2]
    return len(pairs) >= 22
