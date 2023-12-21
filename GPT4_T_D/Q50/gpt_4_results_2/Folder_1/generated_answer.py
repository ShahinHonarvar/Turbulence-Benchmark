
from collections import Counter

def if_contains_anagrams(lst):
    # to store all anagrams in a list
    anagrams = []
    # looping the list
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # if strings are anagrams and of length greater than or equal to 3
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                anagrams.append((lst[i], lst[j]))
    # checking if the count of anagram pairs is 96
    if len(anagrams) >= 96:
        return True
    else:
        return False
