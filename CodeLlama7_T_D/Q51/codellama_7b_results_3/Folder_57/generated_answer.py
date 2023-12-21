
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    num_anagrams = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_anagrams += 1
    # Return True if there are at most 74 pairs of anagrams in the list; otherwise, return False.
    return num_anagrams <= 74
