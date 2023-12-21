
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - 85)):
        # Extract the substring of size 86 starting at position i
        substring = string[i:i+86]

        # Check if the substring is already in the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of substrings
    return substrings
