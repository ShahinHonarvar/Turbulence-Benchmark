
def if_contains_anagrams(str_list):
    from collections import defaultdict
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    str_dict = defaultdict(list)
    for str in str_list:
        if len(str) >= 3:
            str_dict[''.join(sorted(str.lower()))].append(str)
    for k, v in str_dict.items():
        if len(v) > 1:
            anagram_count += len(v)*(len(v) - 1) // 2
        if anagram_count >= 68:
            return True
    return False
