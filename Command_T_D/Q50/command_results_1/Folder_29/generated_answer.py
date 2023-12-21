import collections
def if_contains_anagrams(s):
    anagrams = collections.defaultdict(list)
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j]: continue
            elif len(s[i]) >= 3:
                anagrams[s[i]].append(s[j])
                anagrams[s[j]].append(s[i])
    return len(anagrams) >= 35
