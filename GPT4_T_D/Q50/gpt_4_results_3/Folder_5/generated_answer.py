
def if_contains_anagrams(input_list):
    from collections import Counter
    pair_dict = Counter(''.join(sorted(word.lower())) for word in input_list if len(word) >= 3)
    anagram_pairs = sum(count*(count-1)//2 for count in pair_dict.values())
    return anagram_pairs >= 21
