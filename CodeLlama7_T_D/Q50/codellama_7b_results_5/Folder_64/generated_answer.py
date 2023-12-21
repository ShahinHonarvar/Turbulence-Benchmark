
def if_contains_anagrams(strings):
    # Check if there are at least five pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
                if num_pairs >= 5:
                    return True
    return False
