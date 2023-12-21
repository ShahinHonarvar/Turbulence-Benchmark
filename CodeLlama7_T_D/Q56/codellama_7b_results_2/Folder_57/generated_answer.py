
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 59)):

        # Extract a substring of length 60 from the input string
        substring = input_string[i:i+60]

        # If the substring is not already in the list of substrings, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    return substrings
