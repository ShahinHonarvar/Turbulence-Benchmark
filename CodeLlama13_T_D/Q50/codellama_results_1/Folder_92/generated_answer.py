
def if_contains_anagrams(strs):
    anagram_pairs = []
    for i in range(len(strs)):
        str1 = strs[i].lower()
        for j in range(i+1, len(strs)):
            str2 = strs[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and sorted(str1) == sorted(str2):
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) >= 2
