
def if_contains_anagrams(strings):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings))):
            if sorted(strings[i]) == sorted(strings[j]):
                num_anagrams += 1
    # Check if there are at least 66 pairs of anagrams
    return num_anagrams >= 66
