
def if_contains_anagrams(lst):
    anagram_pairs = []
    
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and lst[i].lower() != lst[j].lower() and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_pairs.append((lst[i], lst[j]))
    
    if len(anagram_pairs) >= 10:
        return True
    else:
        return False
