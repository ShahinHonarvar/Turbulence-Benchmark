
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
        
    count_anagram_pairs = 0
    word_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            word_dict["".join(sorted(word.lower()))] += 1
    for count in word_dict.values():
        count_anagram_pairs += count*(count-1)//2
    if count_anagram_pairs > 19:
        return False
    return True
