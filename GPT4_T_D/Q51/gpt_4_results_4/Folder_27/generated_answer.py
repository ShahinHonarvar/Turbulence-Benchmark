
def if_contains_anagrams(lst):
    from collections import defaultdict
    from itertools import combinations

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    anagram_count = 0
    word_groups = defaultdict(list)

    for word in lst:
        if len(word) >= 3:
            word_groups[''.join(sorted(word.lower()))].append(word)

    for word_list in word_groups.values():
        if len(word_list) > 1:
            for pair in combinations(word_list, 2):
                if is_anagram(*pair):
                    anagram_count += 1
                if anagram_count > 113:
                    return False

    return True
