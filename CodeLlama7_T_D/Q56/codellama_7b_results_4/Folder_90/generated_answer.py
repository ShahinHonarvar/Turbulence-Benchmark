 def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []
    # Loop through each character in the input string
    for i in range(len(input_string) - 130 + 1):
        # Extract the substring of size 130 starting from the current index
        substring = input_string[i:i+130]
        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list
            substrings.append(substring)
    # Return the list of substrings
    return substrings
