
def if_contains_anagrams(my_list):
    # Check if the list is empty or has fewer than four elements
    if len(my_list) < 4:
        return False

    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings and check for anagrams
    for string in my_list:
        # Get the sorted characters of the string
        sorted_chars = ''.join(sorted(string.lower()))

        # Check if the sorted characters are already in the dictionary
        if sorted_chars in anagram_counts:
            # Increment the count for this anagram
            anagram_counts[sorted_chars] += 1

        else:
            # Add the sorted characters to the dictionary with a count of one
            anagram_counts[sorted_chars] = 1

    # Check if there are at least four pairs of anagrams in the list
    for _, count in anagram_counts.items():
        if count >= 4:
            return True

    return False
