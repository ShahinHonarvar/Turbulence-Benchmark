
def all_substring_of_size_n(string, n):
    # Check if the input string is valid
    if not isinstance(string, str) or len(string) < 1:
        raise ValueError("Invalid input string")

    # Check if the substring size is valid
    if n < 1 or n > len(string):
        raise ValueError("Substring size out of range")

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the input string and extract substrings of length n
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring not in substrings:
            substrings.append(substring)

    return substrings
