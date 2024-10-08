
def if_contains_anagrams(string_list):
    # Set of all possible anagrams of the English letters
    anagram_set = set("abcdefghijklmnopqrstuvwxyz".replace(c, "") for c in "abcdefghijklmnopqrstuvwxyz")
    # Number of pairs of anagrams found
    pair_count = 0
    # Loop through each string in the list
    for string in string_list:
        # Convert the string to lowercase
        string = string.lower()
        # If the length of the string is less than three, ignore it
        if len(string) < 3:
            continue

        # Generate all possible anagrams of the string
        for anagram in "".join(sorted(string)):
            # Check if the anagram is a valid word
            if anagram in string_list:
                # If it is, increase the pair count by one
                pair_count += 1

    # Return whether there are at most 48 pairs of anagrams in the list
    return pair_count <= 48
