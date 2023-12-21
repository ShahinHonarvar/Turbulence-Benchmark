
def if_contains_anagrams(str_list):
    from collections import defaultdict

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagrams = defaultdict(list)
    
    for string in str_list:
        if len(string) >= 3:
            anagrams["".join(sorted(string.lower()))].append(string)

    anagram_groups = [anagrams[key] for key in anagrams if len(anagrams[key]) > 1]
    pairs_count = sum(len(group)*(len(group)-1)//2 for group in anagram_groups)

    return pairs_count >= 30
