
def if_contains_anagrams(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return False

    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Remove any non-alphanumeric characters from the string
        string = ''.join(c for c in string if c.isalnum())

        # Sort the string
        string = sorted(string)

        # If the anagram is already in the dictionary, increment its count
        if string in anagram_counts:
            anagram_counts[string] += 1

        # Otherwise, add it to the dictionary with a count of 1
        else:
            anagram_counts[string] = 1

    # Iterate over the dictionary of anagram counts
    for string, count in anagram_counts.items():
        # If the count is greater than 86, return False
        if count > 86:
            return False

    # If none of the conditions are met, return True
    return True
