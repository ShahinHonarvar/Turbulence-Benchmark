
def if_contains_anagrams(strings):
    # Check if any string is an anagram of another string in the list
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                return True

    # Check if there are at most 407 pairs of anagrams in the list
    anagram_pairs = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs.append((i, j))

    if len(anagram_pairs) > 407:
        return False

    # Check if the strings are in a case-insensitive manner
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                if not strings[i].lower() == strings[j].lower():
                    return False

    # If all conditions are met, return true
    return True
