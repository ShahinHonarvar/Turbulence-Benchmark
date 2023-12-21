
def if_contains_anagrams(lst):
    from collections import defaultdict 
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    anagrams = defaultdict(list)
    count_pairs = 0

    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)

    for key in anagrams:
        if len(anagrams[key]) > 1:
            count_pairs += len(anagrams[key])*(len(anagrams[key])-1)//2

    if count_pairs >= 25:
        return True
    else:
        return False
