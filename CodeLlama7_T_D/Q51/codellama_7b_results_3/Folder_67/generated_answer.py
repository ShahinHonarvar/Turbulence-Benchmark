
def if_contains_anagrams(strings):
    # Check if there are at most 5 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings))):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                if num_pairs > 5:
                    return False

    # Check if there are at least three anagrams in the given list

    for i in range(len(strings)):
        if len(set(sorted(strings[i]))) < 3:
            return False

    return True
