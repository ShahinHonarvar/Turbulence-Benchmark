
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for str in str_list:
        # Convert the string to lowercase
        lowercase_str = str.lower()

        # If the string has at least three characters,
        if len(lowercase_str) >= 3:
            # Create a sorted version of the string
            sorted_str = "".join(sorted(lowercase_str))

            # Increment the count for this anagram
            anagram_counts[sorted_str] = anagram_counts.get(sorted_str, 0) + 1

    # Check if there are at least 8 pairs of anagrams in the list
    return len([anagram for anagram in anagram_counts if anagram_counts[anagram] >= 2]) >= 8
