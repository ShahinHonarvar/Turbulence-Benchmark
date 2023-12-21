import collections
def if_contains_anagrams(texts):
    result = False
    for s in texts:
        anagrams = collections.Counter(s.lower())
        for i in range(3, len(s)):
            if anagrams.get(s[i-3:i+4].lower(), 0) > 1:
                result = True
                break
    return result
