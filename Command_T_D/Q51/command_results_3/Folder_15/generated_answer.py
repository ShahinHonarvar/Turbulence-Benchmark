import collections
def if_contains_anagrams(s):
    anagrams = collections.defaultdict(list)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            str1 = s[i].lower()
            str2 = s[j].lower()
            for c in str1:
                if str2[str2.lower().index(c)] != c:
                    break
            else:
                anagrams[str1].append(str2)
                anagrams[str2].append(str1)
    return len(anagrams) <= 20
