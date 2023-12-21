
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each possible starting index in the string
    for i in range(len(s)):

        # Initialize an empty string to store the current substring
        current_substring = ""

        # Iterate over each character in the string, starting at the current index
        for j in range(i, len(s)):

            # Add the current character to the current substring
            current_substring += s[j]

            # If the length of the current substring is equal to n (27), add it to the list of substrings
            if len(current_substring) == n:
                substrings.append(current_substring)

    # Return the list of all distinct substrings of size n in the given string, or an empty list if no such substrings exist
    return substrings
