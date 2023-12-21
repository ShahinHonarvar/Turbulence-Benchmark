
def if_contains_anagrams(strings):
    # Check if there are at most 26 pairs of anagrams in the list
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i]) == sorted(strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 26:
                    return False

    # Check if the strings have a length of at least three

    for string in strings:
        if len(string) < 3:
            return False

    # Compare the strings in a case-insensitive manner

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i].lower() == strings[j].lower():
                return True

    return False
