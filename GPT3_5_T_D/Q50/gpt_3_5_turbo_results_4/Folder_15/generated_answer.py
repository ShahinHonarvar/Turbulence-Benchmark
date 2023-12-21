
def if_contains_anagrams(strings):
    from collections import Counter
    anagram_pairs = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and strings[i].lower() == strings[j].lower():
                counter_i = Counter(strings[i].lower())
                counter_j = Counter(strings[j].lower())
                
                if counter_i == counter_j:
                    anagram_pairs += 1
                    
                    if anagram_pairs >= 4:
                        return True
    
    return False
