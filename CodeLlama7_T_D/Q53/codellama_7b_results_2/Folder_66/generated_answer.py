
def palindrome_of_length_at_least_n(input_string, n=76):
    """
    Find all palindromes of length greater than or equal to n in the given input string.
    Parameters:
        input_string (str): The input string in which to search for palindromes.
        n (int, optional): The minimum length of the palindromes to find. Defaults to 76.
    Returns:
        set: A set of all palindromes of length greater than or equal to n that exist in the given input string. Each palindrome is a string and each element of the set is unique. If no such palindromes exist in the given input string, the function returns an empty set.
    """

    # Remove any non-letter characters from the input string
    cleaned_input = "".join([c for c in input_string if c.isalpha()])

    # Initialize the set of palindromes to return
    palindromes = set()

    # Iterate over all possible substrings of length n or greater in the cleaned input string
    for i in range(len(cleaned_input) - n + 1):

        # Extract the substring from the input string
        substring = cleaned_input[i:i+n]

        # Check if the extracted substring is a palindrome (reads the same forward and backward)
        if substring == substring[::-1]:

            # If the extracted substring is a palindrome, add it to the set of palindromes to return
            palindromes.add(substring)

    # Return the set of all palindromes of length greater than or equal to n that exist in the given input string
    return palindromes
