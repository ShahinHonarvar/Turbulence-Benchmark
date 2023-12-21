 def all_substring_of_size_n(s):
    # Initialize an empty list to store substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):

        # Loop through each character in the remaining part of the string
        for j in range(i + 1, len(s) + 1):

            # Check if the substring has length equal to n (69)
            if j - i == n:

                # Add the substring to the list of substrings
                substrings.append(s[i:j])

    # Return the list of substrings
    return substrings
