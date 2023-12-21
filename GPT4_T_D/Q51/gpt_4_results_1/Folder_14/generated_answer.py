
def if_contains_anagrams(lst):
    from collections import Counter
    
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i])>2 and len(lst[j])>2 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagram_pairs += 1
    return anagram_pairs <= 474
