
from collections import Counter

def if_contains_anagrams(lst):
    cleaned_lst = [''.join(sorted(word.lower())) for word in lst if len(word)>=3]
    counter_obj = Counter(cleaned_lst)
    anagram_pairs = sum([freq*(freq-1)//2 for freq in counter_obj.values()])
    return anagram_pairs <= 67
