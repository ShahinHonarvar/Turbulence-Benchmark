
def all_substring_of_size_n(string, n):
    """
    Return the list of all distinct substrings of length n in string.
    If no such substrings exist in the given string, return an empty list.
    The order of the substrings in the returned list does not matter.
    """

    # Initialize result list and counter for unique substrings

    result = []

    count = 0

    # Iterate over all possible starting positions in the string

    for i in range(len(string) - n + 1):

        # Extract substring of length n from current position

        substr = string[i:i+n]

        # Check if substring is already in result list

        if substr not in result:

            # Add substring to result list and increment counter for unique substrings

            result.append(substr)

            count += 1

    # Return result list with all distinct substrings of length n

    return result
