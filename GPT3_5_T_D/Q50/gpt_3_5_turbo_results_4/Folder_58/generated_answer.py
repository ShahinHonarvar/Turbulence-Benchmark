
def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_pairs += 1
    if anagram_pairs >= 411:
        return True
    else:
        return False
