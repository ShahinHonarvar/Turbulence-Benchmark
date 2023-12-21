
def if_contains_anagrams(strings_list):
    from collections import defaultdict

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagrams_dict = defaultdict(list)

    for s in strings_list:
        if len(s) >= 3:
            anagrams_dict[''.join(sorted(s.lower()))].append(s)

    pairs_count = sum(len(v)*(len(v)-1)//2 for v in anagrams_dict.values())

    return pairs_count >= 136
