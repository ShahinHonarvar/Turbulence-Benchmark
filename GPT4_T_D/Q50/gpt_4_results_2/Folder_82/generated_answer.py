
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    pairs = 0
    for values in anagram_dict.values():
        x = len(values)
        pairs += (x*(x-1))//2
    
    if pairs >= 276:
        return True
    else:
        return False
