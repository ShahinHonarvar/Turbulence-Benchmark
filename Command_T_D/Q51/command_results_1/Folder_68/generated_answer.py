import collections
def if_contains_anagrams(texts):
    letters = set("qwertyuiopasdfghjklzxcvbnm")
    anagrams = collections.defaultdict(list)
    for s in texts:
        s = s.lower()
        for i in range(len(s) - 2):
            key = s[:i] + s[i+1:]
            if key in anagrams:
                anagrams[key].append(s)
            elif len(anagrams[key]) < 94:
                anagrams[key] = [s]
            else:
                return False
    return True
