
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = ''.join(sorted(strings[i].lower()))
            s2 = ''.join(sorted(strings[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3:
                if s1 == s2:
                    anagram_pairs += 1
                    if anagram_pairs > 54:
                        return False
    return True
