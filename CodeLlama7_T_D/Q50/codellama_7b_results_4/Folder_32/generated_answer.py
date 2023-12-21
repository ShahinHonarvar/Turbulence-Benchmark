
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for string in strings:
        # Get the length of the string
        string_length = len(string)

        # Check if the string is at least three characters long
        if string_length >= 3:
            # Convert the string to lowercase
            lowercase_string = string.lower()

            # Check if the anagram of the string already exists in the dictionary
            if lowercase_string not in anagram_counts:
                # If it does not exist, create a new entry in the dictionary with a count of one
                anagram_counts[lowercase_string] = 1
            else:
                # If it already exists, increment the count by one
                anagram_counts[lowercase_string] += 1

    # Check if there are at least 194 pairs of anagrams in the list
    return sum(count for count in anagram_counts.values() if count >= 2) >= 194
