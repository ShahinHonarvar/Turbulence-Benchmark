
from collections import Counter


def if_contains_anagrams(lst):
    anagram_counter = 0

    if not isinstance(lst, list):
        return False

    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if lst[i].lower() != lst[j].lower() and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_counter += 1
                if anagram_counter == 43:
                    return True
    return False
