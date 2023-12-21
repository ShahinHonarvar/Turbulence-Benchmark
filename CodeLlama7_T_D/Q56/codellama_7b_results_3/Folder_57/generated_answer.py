
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):
        # Extract the substring of length n starting at index i
        substring = string[i:i+n]

        # If the substring is already in the list, skip it
        if substring in substrings:
            continue


        # Add the substring to the list
        substrings.append(substring)

    return substrings
