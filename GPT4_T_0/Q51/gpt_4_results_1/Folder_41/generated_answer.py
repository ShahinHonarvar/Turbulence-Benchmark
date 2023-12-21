
def if_contains_anagrams(lst):
    anagram_pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_pairs.append((lst[i], lst[j]))
    if len(anagram_pairs) <= 52:
        return True
    else:
        return False
