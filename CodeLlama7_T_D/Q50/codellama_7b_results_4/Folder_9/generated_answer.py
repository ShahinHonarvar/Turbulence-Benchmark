
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings))):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_pairs += 1
                # If there are at least 66 pairs of anagrams in the list, return True
                if num_pairs >= 66:
                    return True

    # If there are no anagram pairs in the list, return False

    return False
