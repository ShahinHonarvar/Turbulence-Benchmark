
def if_contains_anagrams(strings):
    # Check if there are at least 7 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
    return num_pairs >= 7
