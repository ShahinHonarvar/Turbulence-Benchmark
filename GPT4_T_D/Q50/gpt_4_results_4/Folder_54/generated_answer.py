
def if_contains_anagrams(lst):
    from collections import defaultdict
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    anagrams = defaultdict(list)
    for i, word in enumerate(lst):
        if len(word) >= 3:
            for key in anagrams:
                if is_anagram(word, key):
                    anagrams[key].append(word)
                    break
            else:
                anagrams[word].append(word)
    anagram_pairs = sum(len(val)*(len(val)-1)//2 for val in anagrams.values())
    return anagram_pairs >= 74
