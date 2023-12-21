
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:

        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is at least three characters long
        if len(string) >= 3:

            # Sort the characters in the string
            sorted_chars = ''.join(sorted(string))

            # Increment the count for this anagram
            anagram_counts[sorted_chars] = anagram_counts.get(sorted_chars, 0) + 1

    # Check if there are at least 57 pairs of anagrams in the list
    num_anagrams = len(anagram_counts)
    num_pairs = 0

    for anagram in anagram_counts:

        if anagram_counts[anagram] >= 2:

            num_pairs += 1


    return num_pairs >= 57
