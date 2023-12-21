
def if_contains_anagrams(lst):
    from collections import defaultdict
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagrams_count = 0
    freq_dict = defaultdict(list)
    for string in lst:
        if len(string) >= 3:
            freq_dict["".join(sorted(string.lower()))].append(string)
    
    for val in freq_dict.values():
        if len(val) > 1:
            anagrams_count += len(val) // 2
        if anagrams_count > 8:
            return False

    return True
