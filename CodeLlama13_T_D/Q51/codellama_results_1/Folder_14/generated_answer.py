
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = ''.join(sorted(list(strings[i].lower())))
            str2 = ''.join(sorted(list(strings[j].lower())))
            if len(str1) >= 3 and len(str2) >= 3 and str1 != str2 and sorted(str1) == sorted(str2):
                anagram_pairs += 1
    return anagram_pairs <= 474
