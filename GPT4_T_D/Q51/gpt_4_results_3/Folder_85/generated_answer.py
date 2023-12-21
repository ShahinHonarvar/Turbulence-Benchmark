
def if_contains_anagrams(str_list):
    from collections import Counter
    str_list = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    count_dict = Counter(str_list)
    anagram_pairs = sum([count*(count-1)//2 for count in count_dict.values()])
    return anagram_pairs <= 276
