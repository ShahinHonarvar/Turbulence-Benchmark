
def all_substring_of_size_n(s, n):
    # Check if the input string and size are valid
    if len(s) < n or n < 0:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each substring of length n in the input string
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        # Check if the substring is already in the list
        if substring not in substrings:
            substrings.append(substring)

    return substrings
