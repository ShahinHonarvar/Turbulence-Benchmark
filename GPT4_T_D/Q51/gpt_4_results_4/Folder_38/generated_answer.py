
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    def is_anagram(a, b):
        return sorted(list(a.lower())) == sorted(list(b.lower()))

    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
    return count <= 416
