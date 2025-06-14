
def if_contains_anagrams(strings):
    # Check if there are at most 64 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                if num_pairs > 64:
                    return False
    return True
