
def if_contains_anagrams(strings):
    from collections import defaultdict
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagrams = defaultdict(list)
    for string in strings: 
        if len(string) >= 3: 
            anagrams[''.join(sorted(string.lower()))].append(string)
    pairs = [len(v)*(len(v)-1)/2 for v in anagrams.values() if len(v) > 1]
    if sum(pairs) >= 85:
        return True
    else:
        return False
