
def if_contains_anagrams(my_list):
    # Create a dictionary to keep track of the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram
        if len(lowercase_string) >= 3:
            # If the string is a valid anagram, add it to the dictionary of anagram counts
            if lowercase_string not in anagram_counts:
                anagram_counts[lowercase_string] = 1

            # Increment the count for this anagram
            else:
                anagram_counts[lowercase_string] += 1

    # Check if there are at most 97 pairs of anagrams in the list
    return len(anagram_counts) <= 97
