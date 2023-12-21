
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams_dict[sorted_word].append(word)
    
    pair_count = sum(len(value)*(len(value)-1)//2 for value in anagrams_dict.values())
    return pair_count <= 85
