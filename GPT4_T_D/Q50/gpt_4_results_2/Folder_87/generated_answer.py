
def if_contains_anagrams(lst):
    from collections import defaultdict

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    pairs = 0
    str_dict = defaultdict(list)
    
    for str_ in lst:
        if len(str_) >= 3:
            str_dict[''.join(sorted(str_))].append(str_)
    
    for sorted_str, words in str_dict.items():
        if len(words) >= 2:
            pairs += len(words) * (len(words) - 1) // 2
            
    return pairs >= 88
