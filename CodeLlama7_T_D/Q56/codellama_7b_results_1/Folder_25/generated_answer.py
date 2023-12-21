
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]

        # Check if the substring already exists in the list
        if substring not in substrings:
            substrings.append(substring)

    return substrings
