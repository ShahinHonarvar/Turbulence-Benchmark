
def if_contains_anagrams(lst):
    n = len(lst)
    anagram_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(lst[i])>=3 and len(lst[j])>=3 and sorted(lst[i].lower())==sorted(lst[j].lower()):
                anagram_pairs += 1
    if anagram_pairs >= 153:
        return True
    else:
        return False
