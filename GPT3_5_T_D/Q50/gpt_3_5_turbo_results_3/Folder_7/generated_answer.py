
import collections

def if_contains_anagrams(strings):
    def is_anagram(a, b):
        return collections.Counter(a.lower()) == collections.Counter(b.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 178:
                    return True
    return False
