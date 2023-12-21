
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):

        # Initialize an empty string to store the current substring
        substring = ""

        # Loop through each character in the substring
        for j in range(i, i + 127):

            # Check if the current character is out of bounds
            if j < len(string):

                # Add the current character to the substring
                substring += string[j]

            else:

                # Break the inner loop if the current character is out of bounds
                break

        # Check if the current substring is not empty
        if substring != "":

            # Add the current substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
