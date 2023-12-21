
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a list of all the possible anagrams of the string
            anagram_list = []

            # Iterate over the characters in the string
            for i in range(len(lowercase_string)):
                # Add the current character to the anagram list
                anagram_list.append(lowercase_string[:i] + lowercase_string[i+1:] )

            # Iterate over the anagrams in the list
            for anagram in anagram_list:
                # Check if the anagram is at least three characters long
                if len(anagram) >= 3:
                    # Add the anagram to the dictionary of counts
                    if anagram not in anagram_counts:
                        anagram_counts[anagram] = 1
                    else:
                        anagram_counts[anagram] += 1

    # Check if there are at least 9 pairs of anagrams in the list
    return len(anagram_counts) >= 9
