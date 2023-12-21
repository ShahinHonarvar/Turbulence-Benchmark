
def if_contains_anagrams(strings):
    # Count the number of anagram pairs
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_pairs += 1
                
     # Return true if there are at least 41 pairs of anagrams in the given list.
    return num_pairs >= 41
