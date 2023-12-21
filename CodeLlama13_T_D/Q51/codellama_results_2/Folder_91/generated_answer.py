
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagrams
    anagrams = set()

    # Iterate over the list of strings
    for s in my_list:
        # Convert the string to lowercase
        ls = s.lower()

        # Check if the length of the string is at least 3
        if len(ls) < 3:
            continue

        # Iterate over the English letters
        for c in "abcdefghijklmnopqrstuvwxyz":
            # Check if the letter appears in the string
            if ls.count(c) > 1:
                # If so, add an anagram to the set
                anagrams.add((ls.replace(c, ""), ls))

    # Return true if there are at most 88 pairs of anagrams in the set
    return len(anagrams) <= 88
