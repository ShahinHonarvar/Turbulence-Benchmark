
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:

            # Create a sorted version of the string
            sorted_string = "".join(sorted(lowercase_string))

            # Increment the count for this anagram
            anagram_counts[sorted_string] = anagram_counts.get(sorted_string, 0) + 1

    # Iterate over the dictionary of anagram counts
    for sorted_string, count in anagram_counts.items():

        # Check if there are at least 312 pairs of anagrams
        if count >= 312:
            return True

    return False
