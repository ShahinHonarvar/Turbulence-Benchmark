
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 1):

        # Extract the substring starting from the current index and ending at length n
        substring = string[i:i+2]

        # Check if the substring is already present in the list
        if substring not in substrings:

            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
