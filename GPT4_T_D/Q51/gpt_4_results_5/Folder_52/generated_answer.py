
def if_contains_anagrams(lst):
    from collections import defaultdict
    def check_anagram(s1,s2):
        return sorted(s1) == sorted(s2)
    pairs = 0
    word_dict = defaultdict(list)
    for word in lst:
        if len(word)>=3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    for key, value in word_dict.items():
        pairs += len(value)*(len(value)-1)//2 
    return pairs <= 43
