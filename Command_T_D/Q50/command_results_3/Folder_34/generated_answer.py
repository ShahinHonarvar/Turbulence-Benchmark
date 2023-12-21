import collections
def if_contains_anagrams(s):
    anagrams = collections.defaultdict(set)
    for word in s:
        for anagram in range(len(word)):
            for c in range(26):
                if word[:anagram] + chr(ord('a') + c) + word[anagram+1:] in anagrams:
                    anagrams[word[:anagram] + chr(ord('a') + c) + word[anagram+1:]].add(word)
    return len(anagrams) >= 25
