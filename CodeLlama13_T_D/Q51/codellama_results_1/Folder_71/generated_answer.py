
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1, s2 = strings[i], strings[j]
            if len(s1) >= 3 and len(s2) >= 3:
                s1_chars = set(s1.lower())
                s2_chars = set(s2.lower())
                if len(s1_chars & s2_chars) == len(s1) == len(s2):
                    anagram_pairs += 1
            if anagram_pairs > 9:
                return False
        return True
