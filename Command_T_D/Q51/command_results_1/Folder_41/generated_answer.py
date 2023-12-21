import collections
def if_contains_anagrams(s):
    dct = collections.defaultdict(list)
    for word in s:
        for i in range(len(word)):
            for j in range(len(word)-1, -1, -1):
                c = word[i] + word[j]
                if c in dct:
                    dct[c].append(word)
                else:
                    dct[c] = [word]
    return len(dct) <= 52
