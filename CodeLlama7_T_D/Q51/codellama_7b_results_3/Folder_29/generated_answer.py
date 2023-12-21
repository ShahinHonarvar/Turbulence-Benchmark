
def if_contains_anagrams(strings):
    # Check if there are at most 318 pairs of anagrams in the given list
    number_of_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                number_of_pairs += 1
                if number_of_pairs > 318:
                    return False

    # If there are at most 318 pairs of anagrams in the given list, return true
    return True
