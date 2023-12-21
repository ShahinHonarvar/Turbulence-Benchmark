
def if_contains_anagrams(string_list):
    from collections import defaultdict
    def create_dict(s):
        return ''.join(sorted(s.lower()))

    anagrams = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            anagrams[create_dict(word)].append(word)
    
    anagram_pairs_count = sum(len(values)*(len(values)-1)//2 for values in anagrams.values())
    return anagram_pairs_count >= 52
