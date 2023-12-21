
def if_contains_anagrams(strs):
    anagram_pairs = 0
    for s1 in strs:
        for s2 in strs:
            if s1 != s2 and len(s1) >= 3 and len(s2) >= 3:
                is_anagram = True
                for c1, c2 in zip(s1.lower(), s2.lower()):
                    if c1 != c2:
                        is_anagram = False
                        break
                if is_anagram:
                    anagram_pairs += 1
                    if anagram_pairs == 24:
                        return True
    return False
