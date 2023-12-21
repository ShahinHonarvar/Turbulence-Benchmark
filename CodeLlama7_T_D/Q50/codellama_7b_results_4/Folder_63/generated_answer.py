
def if_contains_anagrams(strings):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                
    # Return True if there are at least 89 pairs of anagrams in the list; otherwise, return False
    return num_pairs >= 89
