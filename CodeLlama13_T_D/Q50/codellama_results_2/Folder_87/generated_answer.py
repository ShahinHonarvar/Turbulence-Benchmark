
def if_contains_anagrams(strings):
    # Initialize an empty dictionary to store the anagram counts for each string length
    anagram_counts = {}

    # Iterate over the input list of strings
    for s in strings:
        # Ignore strings that are less than 3 characters long
        if len(s) < 3:
            continue

        # Convert the string to lowercase
        lc_s = s.lower()

        # If the string is already present in the dictionary, increment its count by 1
        if lc_s in anagram_counts:
            anagram_counts[lc_s] += 1

        # Otherwise, add a new entry to the dictionary with a count of 1
        else:
            anagram_counts[lc_s] = 1

    # If there are at least 88 pairs of anagrams in the list, return True
    if len(anagram_counts) >= 88:
        return True

    # Otherwise, return False
    return False
