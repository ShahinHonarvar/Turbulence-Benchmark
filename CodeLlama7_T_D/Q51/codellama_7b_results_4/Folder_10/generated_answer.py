
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    num_anagrams = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_anagrams += 1
    # Check if there are at most 21 pairs of anagrams in the list
    return num_anagrams <= 21
