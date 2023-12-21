
def if_contains_anagrams(strings):
    # Check if there are at least 64 pairs of anagrams in the list
    anagram_count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_count += 1
                if anagram_count >= 64:
                    return True
    return False
