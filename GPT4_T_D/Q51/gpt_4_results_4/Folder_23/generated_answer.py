
def if_contains_anagrams(lst):
    from collections import Counter
    anagram_count = 0
    sorted_lst = [''.join(sorted(word.lower())) for word in lst if len(word)>=3]
    frequency_dict = Counter(sorted_lst)
    for key in frequency_dict:
        anagram_count += frequency_dict[key] // 2
    return anagram_count <= 49
