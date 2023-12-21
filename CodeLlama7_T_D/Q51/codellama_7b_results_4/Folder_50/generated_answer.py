
def if_contains_anagrams(strings):
    # Check if there are at most 47 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings))):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                num_pairs += 1
                if num_pairs > 47:
                    return False

    # Check if the anagrams are of length at least three

    for string in strings:
        if len(string) < 3:
            continue

        if sorted(string.lower()) == sorted(string[1:] + string[:-1]).lower()):
            return True

    # No anagrams were found

    return False
