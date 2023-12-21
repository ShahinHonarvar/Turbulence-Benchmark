
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each character in the string
    for i in range(len(string)):

        # Initialize a variable to store the substring
        substring = ""

        # Iterate over each character in the string starting from the current index
        for j in range(i, len(string) + 1):

            # Add the current character to the substring
            substring += string[j - 1]

            # If the length of the substring is equal to 105, add it to the list of substrings
            if len(substring) == 105:
                substrings.append(substring)

                # Break out of the inner loop since we have found a substring of size 105
                break

    # Return the list of substrings
    return substrings
