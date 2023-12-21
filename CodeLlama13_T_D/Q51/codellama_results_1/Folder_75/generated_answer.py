
def if_contains_anagrams(my_list):
    anagram_pairs = []
    for s in my_list:
        if len(s) >= 3:
            anagram = ''.join(sorted(s.lower()))
            if anagram not in anagram_pairs:
                anagram_pairs.append(anagram)
    return len(anagram_pairs) <= 55
