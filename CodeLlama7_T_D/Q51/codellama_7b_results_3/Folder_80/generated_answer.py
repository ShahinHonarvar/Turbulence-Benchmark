
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram of the English letters
        if len(lowercase_string) >= 3 and all(c in 'abcdefghijklmnopqrstuvwxyz' for c in lowercase_string):
            # Convert the string to a list of characters
            char_list = list(lowercase_string)

            # Sort the character list in ascending order
            sorted_char_list = sorted(char_list)

            # Join the sorted character list back into a string
            sorted_string = ''.join(sorted_char_list)

            # Check if the sorted string is already in the anagram counts dictionary
            if sorted_string not in anagram_counts:
                # If it's not in the dictionary, add it with a count of 1
                anagram_counts[sorted_string] = 1

            else:
                # If it is already in the dictionary, increment its count by 1
                anagram_counts[sorted_string] += 1

    # Loop through each key-value pair in the anagram counts dictionary
    for sorted_string, count in anagram_counts.items():
        # Check if the count is greater than 255
        if count > 255:
            # If it is, return false
            return False

    # If we made it this far, there are at most 255 pairs of anagrams in the list
    return True
