
def if_contains_anagrams(strings):
    from collections import Counter
    
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    anagram_count += 1
                    
    return anagram_count >= 50
