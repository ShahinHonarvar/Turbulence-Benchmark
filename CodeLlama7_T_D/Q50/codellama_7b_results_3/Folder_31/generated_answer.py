
def if_contains_anagrams(strings):
    # count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_count += 1
    # return true if there are at least 68 pairs of anagrams in the list
    return anagram_count >= 68
