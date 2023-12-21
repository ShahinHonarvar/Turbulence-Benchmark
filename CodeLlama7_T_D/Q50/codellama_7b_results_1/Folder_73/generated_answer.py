
def if_contains_anagrams(string_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for string in string_list:
        # Get the length of the string
        length = len(string)

        # Check if the length is at least 3
        if length >= 3:
            # Create a lowercase version of the string
            lowercase_string = string.lower()

            # Check if the anagram exists in the dictionary
            if lowercase_string in anagram_counts:
                # Increment the count for this anagram
                anagram_counts[lowercase_string] += 1
            else:
                # Add a new entry to the dictionary
                anagram_counts[lowercase_string] = 1

    # Check if there are at least 91 pairs of anagrams in the list
    return len(anagram_counts) >= 91
