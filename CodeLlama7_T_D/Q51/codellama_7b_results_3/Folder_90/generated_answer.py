
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Sort the characters in the string
            sorted_chars = "".join(sorted(lowercase_string))

            # Increment the count for this anagram
            anagram_counts[sorted_chars] = anagram_counts.get(sorted_chars, 0) + 1

    # Check if there are at most 147 pairs of anagrams in the list
    return len(anagram_counts) <= 147
