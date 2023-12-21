
from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for string1 in list_of_strings:
        if len(string1) < 3:
            continue
        for string2 in list_of_strings:
            if (string1 != string2) and (Counter(string1.lower()) == Counter(string2.lower())):
                count += 1
    if count >= 2 * 98:
        return True
    else:
        return False
