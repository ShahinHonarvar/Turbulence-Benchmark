
def if_contains_anagrams(lst):
    from collections import defaultdict

    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            word_dict[sorted_word].append(word)

    count = 0
    for anagrams in word_dict.values():
        n = len(anagrams)
        count += n * (n-1) / 2

    return True if count >= 50 else False
