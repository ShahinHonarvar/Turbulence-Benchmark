
def if_contains_anagrams(lst):
    from collections import Counter
    lst = ["".join(sorted(word.lower())) for word in lst if len(word)>=3]
    word_freq = list(Counter(lst).values())
    count = 0
    for val in word_freq:
        count += (val*(val-1))//2
    if count >= 153:
        return True
    else:
        return False
