
def if_contains_anagrams(strings):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Loop through the strings in the list
    for i in range(len(strings)):
        # Get the current string
        string1 = strings[i]

        # Check if the string is at least 3 characters long
        if len(string1) >= min_length:
            # Convert the string to lowercase
            string2 = string1.lower()

            # Loop through the remaining strings in the list
            for j in range(i+1, len(strings)):
                # Get the current string
                string3 = strings[j]

                # Check if the string is at least 3 characters long
                if len(string3) >= min_length:
                    # Convert the string to lowercase
                    string4 = string3.lower()

                    # Check if the two strings are anagrams of each other
                    if sorted(string2) == sorted(string4):
                        # Increment the number of anagram pairs found
                        anagram_pairs += 1

                        # Check if the number of anagram pairs found is greater than or equal to 58
                        if anagram_pairs >= 58:
                            # Return true, indicating that there are at least 58 pairs of anagrams in the given list
                            return True
    # Return false, indicating that there are not at least 58 pairs of anagrams in the given list
    return False
