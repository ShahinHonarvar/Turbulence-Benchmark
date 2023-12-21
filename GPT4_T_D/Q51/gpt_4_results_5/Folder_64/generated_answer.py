
def if_contains_anagrams(words_list):
    from collections import Counter
    list_anagrams = []
    for word in words_list:
        word = word.lower()
        if len(word) >= 3:
            list_anagrams.append(''.join(sorted(word)))
    counter = Counter(list_anagrams)
    pair_count = sum([1 for count in counter.values() if count > 1])
    if pair_count <= 59:
        return True
    else:
        return False
