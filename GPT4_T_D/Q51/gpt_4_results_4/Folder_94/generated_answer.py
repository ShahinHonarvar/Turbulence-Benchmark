
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    valid_anagrams = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i])>=3 and len(lst[j])>=3 and is_anagram(lst[i], lst[j]):
                valid_anagrams.append((lst[i], lst[j]))
    if len(valid_anagrams) <= 181:
        return True
    return False
