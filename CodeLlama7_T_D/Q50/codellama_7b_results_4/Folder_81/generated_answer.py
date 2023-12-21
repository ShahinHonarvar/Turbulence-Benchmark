
def if_contains_anagrams(strings):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                num_pairs += 1
    # If there are at least 16 pairs of anagrams in the list, return True
    if num_pairs >= 16:
        return True

    # Otherwise, return False

    else:

        return False
