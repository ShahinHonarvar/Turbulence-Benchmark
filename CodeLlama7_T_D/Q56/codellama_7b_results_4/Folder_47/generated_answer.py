
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Initialize an empty string to store the current substring
        substring = ""

        # Loop through each character in the string starting from the current index
        for j in range(i, len(s) + 1):

            # Add the current character to the substring
            substring += s[j - 1]

            # If the length of the substring is equal to 91, add it to the list of substrings
            if len(substring) == 91:
                substrings.append(substring)

            # If the length of the substring is greater than 91, break out of the inner loop
            elif len(substring) > 91:
                break

    # Return the list of substrings
    return substrings
