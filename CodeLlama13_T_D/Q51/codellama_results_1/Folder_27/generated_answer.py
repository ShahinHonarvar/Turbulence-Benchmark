
def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                s1_sorted = "".join(sorted(s1))
                s2_sorted = "".join(sorted(s2))
                if s1_sorted == s2_sorted:
                    anagram_count += 1
            if anagram_count > 113:
                return False
    return True
