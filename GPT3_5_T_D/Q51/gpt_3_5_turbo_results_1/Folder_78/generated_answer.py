
def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if sorted(word1) == sorted(word2) and len(word1) >= 3:
                anagram_count += 1
                if anagram_count > 70:
                    return False
    return True
