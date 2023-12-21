
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = sum(len(words)*(len(words)-1)//2 for words in anagrams.values())
    return count >= 10
