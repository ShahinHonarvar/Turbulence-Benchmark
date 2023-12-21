
def if_contains_anagrams(strings):
    # Check that there are at most 42 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_pairs += 1
                if num_pairs > 42:
                    return False

    # Check that the strings are at least three letters long

    for string in strings:
        if len(string) < 3:
            return False

    # If all conditions are met, return True

    return True
