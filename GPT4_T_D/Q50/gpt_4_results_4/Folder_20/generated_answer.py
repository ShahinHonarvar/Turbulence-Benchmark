
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    anagram_pairs = sum(len(values)*(len(values)-1)//2 for values in anagrams.values())
    if anagram_pairs >= 64:
        return True
    else:
        return False
