
def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagram_count += 1
                if anagram_count > 38:
                    return False
    return True
