
def if_contains_anagrams(str_list):
    # Check if the list is empty or None
    if str_list is None or len(str_list) == 0:
        return False

    # Create a set to store all the unique strings in the list
    unique_strings = set()

    # Iterate over the list of strings
    for string in str_list:
        # Convert the string to lowercase and remove all whitespace characters
        cleaned_string = string.lower().replace(" ", "")

        # Check if the cleaned string is already in the set of unique strings
        if cleaned_string not in unique_strings:
            # Add the cleaned string to the set of unique strings
            unique_strings.add(cleaned_string)

    # Initialize a variable to store the number of pairs of anagrams found
    num_anagrams = 0

    # Iterate over the list of strings again
    for string in str_list:
        # Convert the string to lowercase and remove all whitespace characters
        cleaned_string = string.lower().replace(" ", "")

        # Check if there are at least three letters in the cleaned string
        if len(cleaned_string) >= 3:
            # Create a list of all the unique substrings in the cleaned string
            unique_substrings = []

            # Iterate over each substring in the cleaned string
            for i in range(len(cleaned_string)):
                # Add the substring to the list of unique substrings if it is not already present
                if cleaned_string[i:] not in unique_substrings:
                    unique_substrings.append(cleaned_string[i:])

            # Iterate over each pair of unique substrings
            for substring1 in unique_substrings:
                for substring2 in unique_substrings:
                    # Check if the two substrings are anagrams of each other
                    if sorted(substring1) == sorted(substring2):
                        # Increment the number of pairs of anagrams found
                        num_anagrams += 1

            # If there are at most 20 pairs of anagrams found, return True
            if num_anagrams <= 20:
                return True

    # Otherwise, return False
    return False
