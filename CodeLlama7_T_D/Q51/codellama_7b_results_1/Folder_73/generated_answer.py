
def if_contains_anagrams(my_list):
    # Create a dictionary to store the number of anagrams for each length
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Get the length of the string
        string_length = len(lowercase_string)

        # If the string is at least three characters long, and it contains only English letters, then add its anagram count to the dictionary
        if string_length >= 3 and lowercase_string.isalpha():
            # Get the number of anagrams for this length
            anagram_count = anagram_counts.get(string_length, 0)

            # Increment the number of anagrams for this length
            anagram_count += 1

            # Add the updated count to the dictionary
            anagram_counts[string_length] = anagram_count

    # Return true if there are at most 279 pairs of anagrams in the given list; otherwise, return false
    return len(anagram_counts) <= 279
