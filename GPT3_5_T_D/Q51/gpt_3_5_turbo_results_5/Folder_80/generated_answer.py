
import collections

def if_contains_anagrams(strings):
    def count_chars(string):
        char_count = collections.defaultdict(int)
        for char in string:
            char_count[char.lower()] += 1
        return char_count

    def is_anagram(string1, string2):
        return count_chars(string1) == count_chars(string2)

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 255:
                    return False
    return True
