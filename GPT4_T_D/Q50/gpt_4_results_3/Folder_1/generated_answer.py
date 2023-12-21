
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    for ind in range(len(lst)):
        for next_ind in range(ind+1, len(lst)):
            if len(lst[ind]) >= 3 and len(lst[next_ind]) >= 3:
                if Counter(lst[ind].lower()) == Counter(lst[next_ind].lower()):
                    anagram_counter += 1
    if anagram_counter >= 96:
        return True
    else:
        return False
