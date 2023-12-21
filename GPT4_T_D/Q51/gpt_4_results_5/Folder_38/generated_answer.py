
def if_contains_anagrams(strings):
    from collections import Counter
    def is_anagram(s, t):
        return Counter(s.lower()) == Counter(t.lower())

    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 416:
                    return False
    return True
