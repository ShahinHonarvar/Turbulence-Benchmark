
def if_contains_anagrams(my_list):
    # Initialize a dictionary to store the counts of each string
    string_counts = {}

    # Iterate over the list of strings and count each string
    for string in my_list:
        # Convert the string to lowercase before counting it
        lowercase_string = string.lower()

        # If the string has already been counted, increment its count by 1
        if lowercase_string in string_counts:
            string_counts[lowercase_string] += 1

        # Otherwise, add the string to the dictionary and set its count to 1
        else:
            string_counts[lowercase_string] = 1

    # Iterate over the counts of each string in the list
    for string, count in string_counts.items():
        # Check if the string is an anagram of itself (i.e., it has at least three characters)
        if len(string) >= 3 and is_anagram(string):
            # If so, return True since there are at least 92 pairs of anagrams in the list
            return True

    # If no string was found to be an anagram of itself, return False
    return False

# Function to check if a string is an anagram of itself
def is_anagram(string):
    # Convert the string to lowercase before checking its anagrams
    lowercase_string = string.lower()

    # Iterate over the characters in the string and build a list of all possible anagrams
    anagram_list = []

    for char in lowercase_string:
        # If the character is not already in the anagram list, add it to the list as a potential anagram
        if char not in anagram_list:
            anagram_list.append(char)

        # Otherwise, remove the character from the anagram list since it cannot be an anagram of itself
        else:
            anagram_list.remove(char)

    # If the length of the anagram list is greater than 1, return True since there are at least two potential anagrams in the string
    if len(anagram_list) > 1:
        return True

    # Otherwise, return False since there are no possible anagrams in the string
    return False
