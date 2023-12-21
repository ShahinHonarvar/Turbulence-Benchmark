import collections
def if_contains_anagrams(s):
    d = collections.Counter(s)
    return (sum(1 for i in range(1, len(s)+1) if s[i] in s[i-1:i+2] and d[s[i]] > 1) <= 97)
