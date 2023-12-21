
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def nCr(n,r):
        return int(fact(n)/(fact(r)*fact(n - r)))

    def fact(n):
        res = 1
        for i in range(2, n + 1):
           res = res * i
        return res

    lst = [x.lower() for x in lst if len(x) >= 3]
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += nCr(len(anagrams[key]),2)

    return count <= 79
