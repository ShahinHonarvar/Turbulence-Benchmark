
def if_contains_anagrams(strings):
    # Check if there are at least 115 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(strings) - 2):
        for j in range(i + 1, len(strings) - 1)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                if num_pairs >= 115:
                    return True
    return False
