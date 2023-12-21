
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 120 + 1):
        # Extract the substring of length 120 starting from index i
        substring = string[i:i+120]

        # Check if the substring is already present in the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 120
    return substrings
