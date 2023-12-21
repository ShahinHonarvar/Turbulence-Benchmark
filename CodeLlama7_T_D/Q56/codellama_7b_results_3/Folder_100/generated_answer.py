
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through the string and check if each substring of length n exists
    for i in range(len(string) - 91):
        substring = string[i:i+92]
        if len(substring) == 92 and substring not in substrings:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
