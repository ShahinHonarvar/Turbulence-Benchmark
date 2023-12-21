 def all_substring_of_size_n(s):
    # Initialize an empty list to store substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(s)):

        # Initialize an empty string to store the current substring
        substring = ""

        # Loop through each character in the input string starting from the current index
        for j in range(i, len(s) + 1):

            # Add the current character to the substring
            substring += s[j - 1]

            # If the length of the substring is equal to 92, add it to the list of substrings
            if len(substring) == 92:
                substrings.append(substring)

    # Return the list of substrings in any order
    return substrings
