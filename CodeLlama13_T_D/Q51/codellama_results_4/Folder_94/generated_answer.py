
def if_contains_anagrams(mylist):
    anagram_pairs = 0
    for s1 in mylist:
        for s2 in mylist:
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1.lower()) == sorted(s2.lower()):
                    anagram_pairs += 1
    return anagram_pairs <= 181
