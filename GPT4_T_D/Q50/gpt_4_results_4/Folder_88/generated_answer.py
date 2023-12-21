
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1, str2 = lst[i].lower(), lst[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_count += 1

    return anagram_count >= 34
