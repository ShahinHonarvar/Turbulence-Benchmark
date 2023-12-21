
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    anagram_length_threshold = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Ignore strings that are not at least three characters long
        if len(string1) < anagram_length_threshold:
            continue

        # Convert both strings to lowercase
        string1 = string1.lower()

        # Iterate over the rest of the list of strings
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Ignore strings that are not at least three characters long
            if len(string2) < anagram_length_threshold:
                continue

            # Convert both strings to lowercase
            string2 = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                # Increment the pair count
                pair_count += 1

                # If there are at least nine pairs of anagrams, return False
                if pair_count >= 97:
                    return False

    # If there are no more than nine pairs of anagrams, return True
    return True
