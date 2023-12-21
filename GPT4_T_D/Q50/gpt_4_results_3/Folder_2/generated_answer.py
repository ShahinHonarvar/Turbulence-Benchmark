
from collections import Counter

def if_contains_anagrams(lis):
    count = 0
    lis = list(map(lambda x: ''.join(sorted(x.lower())), lis))
    word_counts = Counter(lis)
    for word in word_counts:
        if len(word) >= 3:
            count += word_counts[word] * (word_counts[word] - 1) / 2
    if count >= 246:
        return True
    else:
        return False
