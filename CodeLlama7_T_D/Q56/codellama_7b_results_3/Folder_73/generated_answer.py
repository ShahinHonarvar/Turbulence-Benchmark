
def all_substring_of_size_n(string):
    # Create a set to store the distinct substrings of size n
    substrings = set()

    # Loop through each character in the string
    for i in range(len(string) - 19 + 1):
        # Extract the substring of size n starting from index i
        substring = string[i:i+20]

        # If the substring is not empty and does not contain any duplicates, add it to the set of substrings
        if substring != "" and len(substring) == 20 and len(set(substring)) == 20:
            substrings.add(substring)

    # Return the list of all distinct substrings of size n with no duplicate characters
    return list(substrings)
