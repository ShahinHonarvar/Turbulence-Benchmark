
from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)-1):
        string1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            string2 = strings[j].lower()
            if string1 != string2 and len(string1) >= 3 and Counter(string1) == Counter(string2):
                anagram_count += 1
                if anagram_count >= 24:
                    return True
    return False
