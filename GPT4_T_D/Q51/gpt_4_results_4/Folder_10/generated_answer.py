
def if_contains_anagrams(lst):
    anagram_counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_counter += 1
            if anagram_counter > 21:
                return False
    return True
