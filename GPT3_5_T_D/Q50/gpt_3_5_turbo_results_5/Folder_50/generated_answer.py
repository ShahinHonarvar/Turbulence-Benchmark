
def if_contains_anagrams(strings):
    from collections import Counter
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 20:
                        return True
    return False
