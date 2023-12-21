
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        # Get the current string and its anagrams
        curr_string = strings[i]
        curr_anagrams = set()
        for char in "abcdefghijklmnopqrstuvwxyz":
            # Check if the current character is in the current string
            if char in curr_string:
                # Remove the current character from the current string and add it to the anagrams set
                curr_anagrams.add(curr_string.replace(char, ""))
        # Check if there are at most 61 pairs of anagrams in the list
        if len(curr_anagrams) > 61:
            return False

    # If there are no more than 61 pairs of anagrams in the list, return True
    return True
