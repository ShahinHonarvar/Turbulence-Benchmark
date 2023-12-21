
from collections import defaultdict

def if_contains_anagrams(str_list):
    count = defaultdict(int)
    for word in str_list:
        if len(word) >= 3:
            count[''.join(sorted(word.lower()))] += 1
    return sum((value - 1) for value in count.values()) <= 17
