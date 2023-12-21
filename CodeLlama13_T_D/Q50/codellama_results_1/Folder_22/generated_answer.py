
def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        str1 = lst[i].lower()
        for j in range(i+1, len(lst)):
            str2 = lst[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    anagram_count += 1
    return anagram_count >= 72
