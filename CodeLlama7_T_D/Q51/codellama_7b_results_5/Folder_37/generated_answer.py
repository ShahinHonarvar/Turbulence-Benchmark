
def if_contains_anagrams(strings):
    # Create a dictionary to store the number of anagrams for each string
    anagram_counts = {}

    # Iterate over the strings in the list
    for string in strings:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the lowercase string is already in the dictionary of anagram counts
        if lowercase_string not in anagram_counts:
            # If it's not, add it with a count of 1
            anagram_counts[lowercase_string] = 1

        else:
            # If it is, increment the count by 1
            anagram_counts[lowercase_string] += 1

    # Iterate over the dictionary of anagram counts
    for lowercase_string, count in anagram_counts.items():
        # Check if the count is greater than or equal to 3 and less than or equal to 206
        if count >= 3 and count <= 206:
            # If it is, return True
            return True

    # If we make it all the way through the dictionary without returning True, return False
    return False
