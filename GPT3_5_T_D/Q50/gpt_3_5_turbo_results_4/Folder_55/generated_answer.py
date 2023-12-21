
def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagram_count += 1
    return True if anagram_count >= 15 else False
