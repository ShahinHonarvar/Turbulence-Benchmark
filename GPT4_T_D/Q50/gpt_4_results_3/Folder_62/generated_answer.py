
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        
        if len(str1) < 3 or len(str2) < 3:
            return False
        else:
            return sorted(str1) == sorted(str2)

    word_groups = defaultdict(list)

    for word in lst:
        word_groups[tuple(sorted(word.lower()))].append(word)

    anagram_pairs_count = sum(len(words)*(len(words)-1)//2 for words in word_groups.values() if len(words) > 1)
    
    return anagram_pairs_count >= 43
