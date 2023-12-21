
def if_contains_anagrams(words_list):
    from collections import defaultdict
    anagram_pairs = defaultdict(list)

    for word in words_list:
        word = word.lower()
        if len(word) >= 3:
            anagram_pairs[''.join(sorted(word))].append(word)
    
    pair_counter = sum([len(v)*(len(v)-1)//2 for v in anagram_pairs.values() if len(v) > 1])

    return pair_counter >= 312
