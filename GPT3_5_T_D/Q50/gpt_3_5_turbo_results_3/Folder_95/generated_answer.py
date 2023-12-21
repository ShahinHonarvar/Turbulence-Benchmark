
def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and sorted(str1) == sorted(str2):
                anagram_pairs += 1
                if anagram_pairs >= 93:
                    return True
    return False
