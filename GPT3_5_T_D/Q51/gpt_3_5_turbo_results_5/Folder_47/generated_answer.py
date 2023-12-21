
import collections

def if_contains_anagrams(strings):
    count = 0

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return collections.Counter(str1) == collections.Counter(str2)

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    count += 1
            if count > 366:
                return False

    return True
