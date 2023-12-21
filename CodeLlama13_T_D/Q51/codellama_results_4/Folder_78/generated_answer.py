
def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for s1 in str_list:
        for s2 in str_list[str_list.index(s1)+1:]:
            if is_anagram(s1, s2) and len(s1)>=3 and len(s2)>=3:
                anagram_pairs += 1
    return anagram_pairs<=70

def is_anagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    for c in str1.lower():
        if not c in str2.lower():
            return False
    return True
